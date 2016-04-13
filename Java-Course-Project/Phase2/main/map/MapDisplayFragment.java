package ca.ubc.cs.cpsc210.meetup.map;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.Fragment;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.PorterDuff;
import android.graphics.drawable.Drawable;
import android.os.AsyncTask;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONTokener;
import org.osmdroid.DefaultResourceProxyImpl;
import org.osmdroid.ResourceProxy;
import org.osmdroid.api.IGeoPoint;
import org.osmdroid.api.IMapController;
import org.osmdroid.tileprovider.tilesource.TileSourceFactory;
import org.osmdroid.util.GeoPoint;
import org.osmdroid.views.MapView;
import org.osmdroid.views.overlay.ItemizedIconOverlay;
import org.osmdroid.views.overlay.OverlayItem;
import org.osmdroid.views.overlay.OverlayManager;
import org.osmdroid.views.overlay.PathOverlay;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;

import ca.ubc.cs.cpsc210.meetup.R;
import ca.ubc.cs.cpsc210.meetup.model.Building;
import ca.ubc.cs.cpsc210.meetup.model.Course;
import ca.ubc.cs.cpsc210.meetup.model.CourseFactory;
import ca.ubc.cs.cpsc210.meetup.model.Place;
import ca.ubc.cs.cpsc210.meetup.model.PlaceFactory;
import ca.ubc.cs.cpsc210.meetup.model.Section;
import ca.ubc.cs.cpsc210.meetup.model.Student;
import ca.ubc.cs.cpsc210.meetup.model.StudentManager;
import ca.ubc.cs.cpsc210.meetup.util.LatLon;
import ca.ubc.cs.cpsc210.meetup.util.SchedulePlot;

/**
 * Fragment holding the map in the UI.
 */
public class MapDisplayFragment extends Fragment {

    /**
     * Log tag for LogCat messages
     */
    private final static String LOG_TAG = "MapDisplayFragment";

    /**
     * Preference manager to access user preferences
     */
    private SharedPreferences sharedPreferences;

    /**
     * String to know whether we are dealing with MWF or TR schedule.
     * You will need to update this string based on the settings dialog at appropriate
     * points in time. See the project page for details on how to access
     * the value of a setting.
     */
    private String activeDay = "MWF";
    private String foodType = "All";

    /**
     * A central location in campus that might be handy.
     */
    private final static GeoPoint UBC_MARTHA_PIPER_FOUNTAIN = new GeoPoint(49.264865,
            -123.252782);

    /**
     * Meetup Service URL
     * CPSC 210 Students: Complete the string.
     */
    private final String getStudentURL = "http://kramer.nss.cs.ubc.ca:8081/getStudent";

    /**
     * FourSquare URLs. You must complete the client_id and client_secret with values
     * you sign up for.
     */
    private static String FOUR_SQUARE_URL = "https://api.foursquare.com/v2/venues/explore";
    private static String FOUR_SQUARE_CLIENT_ID = "HAOEVY2PF1B5SUM5EHOQ4QI1HP540BJWQ402Y10O1TKHQH4E";
    private static String FOUR_SQUARE_CLIENT_SECRET = "10D4WUOGQ1GESWCJLO4BUV4W1CLYSFEU4DMAWCKRTSANU213";
    private static String MAPQUEST_KEY="Fmjtd%7Cluu82l0a2u%2C2s%3Do5-94zn1z";


    /**
     * Overlays for displaying my schedules, buildings, etc.
     */
    private List<PathOverlay> scheduleOverlay;
    private ItemizedIconOverlay<OverlayItem> buildingOverlay;
    private OverlayItem selectedBuildingOnMap;

    /**
     * View that shows the map
     */
    private MapView mapView;

    /**
     * Access to domain model objects. Only store "me" in the studentManager for
     * the base project (i.e., unless you are doing bonus work).
     */
    private StudentManager studentManager;
    private Student randomStudent = null;
    private Student me = null;
    private static int ME_ID = 999999;
    private PlaceFactory placeFactory;

    private Map<LatLon, String> reviews;

    /**
     * Map controller for zooming in/out, centering
     */
    private IMapController mapController;

    // ******************** Android methods for starting, resuming, ...

    // You should not need to touch this method
    @Override
    public void onActivityCreated(Bundle savedInstanceState) {
        super.onActivityCreated(savedInstanceState);
        setHasOptionsMenu(true);
        sharedPreferences = PreferenceManager
                .getDefaultSharedPreferences(getActivity());
        scheduleOverlay = new ArrayList<PathOverlay>();

        // You need to setup the courses for the app to know about. Ideally
        // we would access a web service like the UBC student information system
        // but that is not currently possible
        initializeCourses();

        // Initialize the data for the "me" schedule. Note that this will be
        // hard-coded for now
        initializeMySchedule();
        placeFactory = PlaceFactory.getInstance();

        // You are going to need an overlay to draw buildings and locations on the map
        buildingOverlay = createBuildingOverlay();
    }

    // You should not need to touch this method
    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (resultCode != Activity.RESULT_OK)
            return;
    }

    // You should not need to touch this method
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        if (mapView == null) {
            mapView = new MapView(getActivity(), null);

            mapView.setTileSource(TileSourceFactory.MAPNIK);
            mapView.setClickable(true);
            mapView.setBuiltInZoomControls(true);
            mapView.setMultiTouchControls(true);

            mapController = mapView.getController();
            mapController.setZoom(mapView.getMaxZoomLevel() - 2);
            mapController.setCenter(UBC_MARTHA_PIPER_FOUNTAIN);
        }

        return mapView;
    }

    // You should not need to touch this method
    @Override
    public void onDestroyView() {
        Log.d(LOG_TAG, "onDestroyView");
        ((ViewGroup) mapView.getParent()).removeView(mapView);
        super.onDestroyView();
    }

    // You should not need to touch this method
    @Override
    public void onDestroy() {
        Log.d(LOG_TAG, "onDestroy");
        super.onDestroy();
    }

    // You should not need to touch this method
    @Override
    public void onResume() {
        Log.d(LOG_TAG, "onResume");
        super.onResume();
    }

    // You should not need to touch this method
    @Override
    public void onPause() {
        Log.d(LOG_TAG, "onPause");
        super.onPause();
    }

    /**
     * Save map's zoom level and centre. You should not need to
     * touch this method
     */
    @Override
    public void onSaveInstanceState(Bundle outState) {
        Log.d(LOG_TAG, "onSaveInstanceState");
        super.onSaveInstanceState(outState);

        if (mapView != null) {
            outState.putInt("zoomLevel", mapView.getZoomLevel());
            IGeoPoint cntr = mapView.getMapCenter();
            outState.putInt("latE6", cntr.getLatitudeE6());
            outState.putInt("lonE6", cntr.getLongitudeE6());
            Log.i("MapSave", "Zoom: " + mapView.getZoomLevel());
        }
    }

    // ****************** App Functionality

    /**
     * Show my schedule on the map. Every time "me"'s schedule shows, the map
     * should be cleared of all existing schedules, buildings, meetup locations, etc.
     */
    public void showMySchedule() {

        // CPSC 210 Students: You must complete the implementation of this method.
        // The very last part of the method should call the asynchronous
        // task (which you will also write the code for) to plot the route
        // for "me"'s schedule for the day of the week set in the Settings

        // Asynchronous tasks are a bit onerous to deal with. In order to provide
        // all information needed in one object to plot "me"'s route, we
        // create a SchedulePlot object and pass it to the asynchrous task.
        // See the project page for more details.
        clearSchedules();
        activeDay = sharedPreferences.getString("dayOfWeek", "MWF");
        SortedSet<Section> sections = me.getSchedule().getSections(activeDay);
        String name = me.getLastName() + "_" + me.getFirstName();
        SchedulePlot mySchedulePlot = new SchedulePlot(sections, name, "#0066FF", R.drawable.ic_action_place);

        // Get a routing between these points. This line of code creates and calls
        // an asynchronous task to do the calls to MapQuest to determine a route
        // and plots the route.
        // Assumes mySchedulePlot is a create and initialized SchedulePlot object


        // UNCOMMENT NEXT LINE ONCE YOU HAVE INSTANTIATED mySchedulePlot
        new GetRoutingForSchedule().execute(mySchedulePlot);
    }

    /**
     * Retrieve a random student's schedule from the Meetup web service and
     * plot a route for the schedule on the map. The plot should be for
     * the given day of the week as determined when "me"'s schedule
     * was plotted.
     */
    public void showRandomStudentsSchedule() {
        // To get a random student's schedule, we have to call the MeetUp web service.
        // Calling this web service requires a network access to we have to
        // do this in an asynchronous task. See below in this class for where
        // you need to implement methods for performing the network access
        // and plotting.
        activeDay = sharedPreferences.getString("dayOfWeek", "MWF");
        new GetRandomSchedule().execute();
    }

    /**
     * Clear all schedules on the map
     */
    public void clearSchedules() {
        randomStudent = null;
        OverlayManager om = mapView.getOverlayManager();
        om.clear();
        scheduleOverlay.clear();
        buildingOverlay.removeAllItems();
        om.addAll(scheduleOverlay);
        om.add(buildingOverlay);
        mapView.invalidate();
    }

    /**
     * Find all possible locations at which "me" and random student could meet
     * up for the set day of the week and the set time to meet and the set
     * distance either "me" or random is willing to travel to meet.
     * A meetup is only possible if both "me" and random are free at the
     * time specified in the settings and each of us must have at least an hour
     * (>= 60 minutes) free. You should display dialog boxes if there are
     * conditions under which no meetup can happen (e.g., me or random is
     * in class at the specified time)
     */
    public void findMeetupPlace() {

        // CPSC 210 students: you must complete this method
        String timeOfBreak = sharedPreferences.getString("timeOfDay", "12");
        activeDay = sharedPreferences.getString("dayOfWeek", "MWF");

        if (randomStudent == null){
            createSimpleDialog("Random student is not initialized!").show();
            return;
        }
        if (!(randomStudent.getSchedule().isAvailable(activeDay, timeOfBreak) &&
                me.getSchedule().isAvailable(activeDay, timeOfBreak))){
            createSimpleDialog("No mutual break time sufficiently long, cannot meet.").show();
        }
        else{
            //initializePlaces();
            placeFactory = PlaceFactory.getInstance();
            if (placeFactory.isEmpty()){
                createSimpleDialog("Need to get places before finding meetup place.").show();
                return;
            }
            int distance = Integer.parseInt(sharedPreferences.getString("placeDistance", "250"));
            LatLon positionOfMe = me.getSchedule().whereAmI(activeDay, timeOfBreak).getLatLon();
            LatLon positionOfTheOther = randomStudent.getSchedule().whereAmI(activeDay, timeOfBreak).getLatLon();
            Set<Place> placesICanGo = placeFactory.findPlacesWithinDistance(positionOfMe, distance);
            Set<Place> placesOtherCanGo = placeFactory.findPlacesWithinDistance(positionOfTheOther, distance);
            placesICanGo.retainAll(placesOtherCanGo); // get the places that both of us can go to within the
            // distance limit.
            if (placesICanGo.isEmpty()){
                createSimpleDialog("Cannot meet with the distance specified. Please choose a longer distance").show();
                return;
            }
            mapView.invalidate(); // Clean previous map overlays.
            String eol = System.getProperty("line.separator");
            for (Place p:placesICanGo){
                String msg = "Distance from me: " + String.valueOf(LatLon.distanceBetweenTwoLatLon(
                        p.getLatLon(), positionOfMe)) + eol + "Distance from random student: " +
                        String.valueOf(LatLon.distanceBetweenTwoLatLon(p.getLatLon(), positionOfTheOther))
                        + eol + "Most popular review: " + reviews.get(p.getLatLon());
                Building convertedPlace = new Building(p.getName(), p.getLatLon());
                plotABuilding(convertedPlace, p.getName(), msg, R.drawable.ic_action_location_found);
            }
            OverlayManager om = mapView.getOverlayManager();
            om.add(buildingOverlay);
            mapView.invalidate();
        }
        
    }

    /**
     * Initialize the PlaceFactory with information from FourSquare
     */
    public void initializePlaces() {
        // CPSC 210 Students: You should not need to touch this method, but
        // you will have to implement GetPlaces below.
        new GetPlaces().execute();
    }


    /**
     * Plot all buildings referred to in the given information about plotting
     * a schedule.
     * @param schedulePlot All information about the schedule and route to plot.
     */
    private void plotBuildings(SchedulePlot schedulePlot) {

        // CPSC 210 Students: Complete this method by plotting each building in the
        // schedulePlot with an appropriate message displayed
        SortedSet<Section> sections = schedulePlot.getSections();
        String color = schedulePlot.getColourOfLine();
        String eol = System.getProperty("line.separator");
        for (Section s:sections){
            String message = "Owner of the Schedule: " + schedulePlot.getName() + eol +"Course information: "
                    + s.getCourse().getCode() + String.valueOf(s.getCourse().getNumber()) + eol +
                    "Section information: " + s.getName() + eol + "Time: " + s.getCourseTime().toString();
            plotABuilding(s.getBuilding(), s.getBuilding().getName(), message, schedulePlot.getIcon());
        }

        // CPSC 210 Students: You will need to ensure the buildingOverlay is in
        // the overlayManager. The following code achieves this. You should not likely
        // need to touch it
        OverlayManager om = mapView.getOverlayManager();
        om.add(buildingOverlay);
        //mapView.invalidate();
    }

    /**
     * Plot a building onto the map
     * @param building The building to put on the map
     * @param title The title to put in the dialog box when the building is tapped on the map
     * @param msg The message to display when the building is tapped
     * @param drawableToUse The icon to use. Can be R.drawable.ic_action_place (or any icon in the res/drawable directory)
     */
    private void plotABuilding(Building building, String title, String msg, int drawableToUse) {
        // CPSC 210 Students: You should not need to touch this method
        OverlayItem buildingItem = new OverlayItem(title, msg,
                new GeoPoint(building.getLatLon().getLatitude(), building.getLatLon().getLongitude()));

        //Create new marker
        Drawable icon = this.getResources().getDrawable(drawableToUse);
        icon.setColorFilter(Color.BLUE, PorterDuff.Mode.MULTIPLY);

        //Set the bounding for the drawable
        icon.setBounds(
                0 - icon.getIntrinsicWidth() / 2, 0 - icon.getIntrinsicHeight(),
                icon.getIntrinsicWidth() / 2, 0);

        //Set the new marker to the overlay
        buildingItem.setMarker(icon);
        buildingOverlay.addItem(buildingItem);
    }



    /**
     * Initialize your schedule by coding it directly in. This is the schedule
     * that will appear on the map when you select "Show My Schedule".
     */
    private void initializeMySchedule() {
        // CPSC 210 Students; Implement this method
        studentManager = new StudentManager();
        studentManager.addStudent("Feng", "Qingyuan", ME_ID);
        studentManager.addSectionToSchedule(ME_ID, "CPSC", 210, "202");
        studentManager.addSectionToSchedule(ME_ID, "MATH", 200, "201");
        studentManager.addSectionToSchedule(ME_ID, "PHYS", 203, "201");
        studentManager.addSectionToSchedule(ME_ID, "SCIE", 113, "213");
        me = studentManager.get(ME_ID);

    }

    /**
     * Helper to create simple alert dialog to display message
     *
     * @param msg message to display in alert dialog
     * @return the alert dialog
     */
    private AlertDialog createSimpleDialog(String msg) {
        // CPSC 210 Students; You should not need to modify this method
        AlertDialog.Builder dialogBldr = new AlertDialog.Builder(getActivity());
        dialogBldr.setMessage(msg);
        dialogBldr.setNeutralButton(R.string.ok, null);

        return dialogBldr.create();
    }

    /**
     * Create the overlay used for buildings. CPSC 210 students, you should not need to
     * touch this method.
     * @return An overlay
     */
    private ItemizedIconOverlay<OverlayItem> createBuildingOverlay() {
        ResourceProxy rp = new DefaultResourceProxyImpl(getActivity());

        ItemizedIconOverlay.OnItemGestureListener<OverlayItem> gestureListener =
                new ItemizedIconOverlay.OnItemGestureListener<OverlayItem>() {

            /**
             * Display building description in dialog box when user taps stop.
             *
             * @param index
             *            index of item tapped
             * @param oi
             *            the OverlayItem that was tapped
             * @return true to indicate that tap event has been handled
             */
            @Override
            public boolean onItemSingleTapUp(int index, OverlayItem oi) {

                new AlertDialog.Builder(getActivity())
                        .setPositiveButton(R.string.ok, new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface arg0, int arg1) {
                                if (selectedBuildingOnMap != null) {
                                    mapView.invalidate();
                                }
                            }
                        }).setTitle(oi.getTitle()).setMessage(oi.getSnippet())
                        .show();

                selectedBuildingOnMap = oi;
                mapView.invalidate();
                return true;
            }

            @Override
            public boolean onItemLongPress(int index, OverlayItem oi) {
                // do nothing
                return false;
            }
        };

        return new ItemizedIconOverlay<OverlayItem>(
                new ArrayList<OverlayItem>(), getResources().getDrawable(
                R.drawable.ic_action_place), gestureListener, rp);
    }


    /**
     * Create overlay with a specific color
     * @param colour A string with a hex colour value
     */
    private PathOverlay createPathOverlay(String colour) {
        // CPSC 210 Students, you should not need to touch this method
        PathOverlay po = new PathOverlay(Color.parseColor(colour),
                getActivity());
        Paint pathPaint = new Paint();
        pathPaint.setColor(Color.parseColor(colour));
        pathPaint.setStrokeWidth(4.0f);
        pathPaint.setStyle(Paint.Style.STROKE);
        po.setPaint(pathPaint);
        return po;
    }

   // *********************** Asynchronous tasks

    /**
     * This asynchronous task is responsible for contacting the Meetup web service
     * for the schedule of a random student. The task must plot the retrieved
     * student's route for the schedule on the map in a different colour than the "me" schedule
     * or must display a dialog box that a schedule was not retrieved.
     */
    private class GetRandomSchedule extends AsyncTask<Void, Void, SchedulePlot> {

        // Some overview explanation of asynchronous tasks is on the project web page.

        @Override
        protected void onPreExecute() {
        }

        @Override
        protected SchedulePlot doInBackground(Void... params) {

            // CPSC 210 Students: You must complete this method. It needs to
            // contact the Meetup web service to get a random student's schedule.
            // If it is successful in retrieving a student and their schedule,
            // it needs to remember the student in the randomStudent field
            // and it needs to create and return a schedulePlot object with
            // all relevant information for being ready to retrieve the route
            // and plot the route for the schedule. If no random student is
            // retrieved, return null.
            //
            // Note, leave all determination of routing and plotting until
            // the onPostExecute method below.
            SchedulePlot randomStudentSP = new SchedulePlot(null, null, null, 0);
            StudentManager studentManager = new StudentManager();
            try {
                JSONObject randomStudentJson = new JSONObject(makeRoutingCall(getStudentURL));
                if (randomStudentJson == null) return null;
                int studentId = Integer.parseInt(randomStudentJson.getString("Id"));
                String firstName = randomStudentJson.getString("FirstName");
                String lastName = randomStudentJson.getString("LastName");
                studentManager.addStudent(lastName, firstName, studentId);
                JSONArray sectionsJson = randomStudentJson.getJSONArray("Sections");
                SortedSet<Section> sections = new TreeSet<Section>();
                int length = sectionsJson.length();
                for (int i = 0; i<length; i++ ){
                    String courseName = sectionsJson.getJSONObject(i).getString("CourseName");
                    int courseNumber = Integer.parseInt(sectionsJson.getJSONObject(i).getString("CourseNumber"));
                    String sectionId = sectionsJson.getJSONObject(i).getString("SectionName");
                    studentManager.addSectionToSchedule(studentId, courseName, courseNumber, sectionId);
                    CourseFactory coursefactory = CourseFactory.getInstance();
                    Section sect = coursefactory.getCourse(courseName, courseNumber).getSection(sectionId);
                    if (sect.getDayOfWeek().equalsIgnoreCase(activeDay))
                        sections.add(sect); // ensures that only the sections held on activeDay are included in schedulePlot.
                }
                randomStudent = studentManager.get(studentId);
                randomStudentSP = new SchedulePlot(sections, lastName + "_" + firstName,
                        "#FFFF00", R.drawable.ic_action_place);

            } catch (JSONException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }

            if (randomStudentSP != null){
                SortedSet<Section> sections = randomStudentSP.getSections();
                if (!sections.isEmpty()){

                    List<GeoPoint> route = new ArrayList<GeoPoint>();
                    List<LatLon> positions = new ArrayList<LatLon>(); // positions store the coordinates
                    // of the classroom of each section.
                    for (Section s:sections){
                        LatLon position = s.getBuilding().getLatLon();
                        positions.add(position);
                    }

                    if (sections.size() == 1){ //Scenario of only one section on the day: only one point.
                        route.add(new GeoPoint(positions.get(0).getLatitude(), positions.get(0).getLongitude()));
                        randomStudentSP.setRoute(route);
                    }
                    else if (sections.size() > 1){ // Several sections on the day: perhaps more points than one.
                        for(int i = 0; i < positions.size() - 1; i++){
                            String startLat = String.valueOf(positions.get(i).getLatitude());
                            String startLon = String.valueOf(positions.get(i).getLongitude());
                            String endLat = String.valueOf(positions.get(i+1).getLatitude());
                            String endLon = String.valueOf(positions.get(i+1).getLongitude());

                            if (startLat.equals(endLat) && startLon.equals(endLon)){
                                if (i == positions.size()-2 && route.size() == 0)
                                    route.add(new GeoPoint(positions.get(i).getLatitude(), positions.get(i).getLongitude()));
                                continue;// No need to go through following steps, as the position is not moved.
                            }

                            route.add(new GeoPoint(positions.get(i).getLatitude(), positions.get(i).getLongitude()));

                            String url = "http://open.mapquestapi.com/directions/v2/route?key=" + MAPQUEST_KEY +
                                    "&generalize=0&routeType=pedestrian" + "&from=" + startLat + ","+startLon +
                                    "&to=" + endLat + "," + endLon;

                            try {
                                JSONObject returned = new JSONObject(makeRoutingCall(url));
                                JSONArray shapePoints = returned.getJSONObject("route").getJSONObject("shape")
                                        .getJSONArray("shapePoints");
                                int length = shapePoints.length()/2;// gives back the time of maneuvers needed in the route.
                                for (int j = 0; j < length; j++){
                                    double lat = shapePoints.getDouble( 2*j );
                                    double lon = shapePoints.getDouble( 2*j+1 );
                                    route.add(new GeoPoint(lat, lon));
                                }
                                route.add(new GeoPoint(positions.get(i+1).getLatitude(), positions.get(i+1).getLongitude()));
                            }
                            catch (JSONException e) {e.printStackTrace();}
                            catch (IOException e) { e.printStackTrace();}
                        }
                        randomStudentSP.setRoute(route);
                    }
                }
            }
            return randomStudentSP; //TODO: might be finished.
        }

        /**
         * An example helper method to call a web service
         */
        private String makeRoutingCall(String httpRequest) throws MalformedURLException, IOException {
            URL url = new URL(httpRequest);
            HttpURLConnection client = (HttpURLConnection) url.openConnection();
            InputStream in = client.getInputStream();
            BufferedReader br = new BufferedReader(new InputStreamReader(in));
            String returnString = br.readLine();
            client.disconnect();
            return returnString;
        }

        @Override
        protected void onPostExecute(SchedulePlot schedulePlot) {
            // CPSC 210 students: When this method is called, it will be passed
            // whatever schedulePlot object you created (if any) in doBackground
            // above. Use it to plot the route.
            if (schedulePlot == null) {
                createSimpleDialog("SchedulePlot of random student on this day is null.").show();
                return;
            }
            SortedSet<Section> sections = schedulePlot.getSections();
            if (sections.isEmpty()) {
                createSimpleDialog("Random student " + schedulePlot.getName() + " has no sections on the day!").show();
                return; //No sections on the day, thus no points to plot, directly return.
            }

            if(sections.size() == 1){
                createSimpleDialog("Random student " + schedulePlot.getName() +
                        " only has one section on the day, no routes.").show();
            }

            List<GeoPoint> route = schedulePlot.getRoute();

            if (route.isEmpty()){
                createSimpleDialog("No route to plot!").show();
                return;
            }
            else{
                PathOverlay po = createPathOverlay(schedulePlot.getColourOfLine());

                for (GeoPoint p:route){
                    po.addPoint(p);
                }
                scheduleOverlay.add(po);
                OverlayManager om = mapView.getOverlayManager();
                om.addAll(scheduleOverlay);
                plotBuildings(schedulePlot);
                mapView.invalidate(); // cause map to redraw
            }
        }
    }

    /**
     * This asynchronous task is responsible for contacting the MapQuest web service
     * to retrieve a route between the buildings on the schedule and for plotting any
     * determined route on the map.
     */
    private class GetRoutingForSchedule extends AsyncTask<SchedulePlot, Void, SchedulePlot> {

        @Override
        protected void onPreExecute() {
        }

        @Override
        protected SchedulePlot doInBackground(SchedulePlot... params) {

            // The params[0] element contains the schedulePlot object
            SchedulePlot scheduleToPlot = params[0];

            // CPSC 210 Students: Complete this method. This method should
            // call the MapQuest webservice to retrieve a List<GeoPoint>
            // that forms the routing between the buildings on the
            // schedule. The List<GeoPoint> should be put into
            // scheduleToPlot object.
            SortedSet<Section> sections = scheduleToPlot.getSections();
            if (sections.isEmpty()) {
                return scheduleToPlot; //Not sure whether this really works.
            }
            List<LatLon> positions = new ArrayList<LatLon>();
            for (Section s:sections){
                LatLon position = s.getBuilding().getLatLon();
                positions.add(position);
            }

            List<GeoPoint> route = new ArrayList<GeoPoint>();
            route.add(new GeoPoint(positions.get(0).getLatitude(), positions.get(0).getLongitude()));

            if(positions.size() == 1){
                scheduleToPlot.setRoute(route);
                return scheduleToPlot;
            }

            for(int i = 0; i < positions.size() - 1; i++){
                String startLat = String.valueOf(positions.get(i).getLatitude());
                String startLon = String.valueOf(positions.get(i).getLongitude());
                String endLat = String.valueOf(positions.get(i+1).getLatitude());
                String endLon = String.valueOf(positions.get(i+1).getLongitude());
                String url = "http://open.mapquestapi.com/directions/v2/route?key=" + MAPQUEST_KEY +
                        "&generalize=0&routeType=pedestrian" + "&from=" + startLat + ","+startLon +
                        "&to=" + endLat + "," + endLon;
                if (i > 0){
                    route.add(new GeoPoint(positions.get(i).getLatitude(), positions.get(i).getLongitude()));
                }
                try {
                    JSONObject returned = new JSONObject(new JSONTokener(makeRoutingCall(url)));
                    JSONArray shapePoints = returned.getJSONObject("route").getJSONObject("shape")
                            .getJSONArray("shapePoints");
                    int length = shapePoints.length()/2;// gives back the time of maneuvers needed in the route.
                    for (int j = 0; j < length; j++){
                        double lat = shapePoints.getDouble( 2*j );
                        double lon = shapePoints.getDouble( 2*j+1 );
                        route.add(new GeoPoint(lat, lon));
                    }
                    route.add(new GeoPoint(positions.get(i+1).getLatitude(), positions.get(i+1).getLongitude()));
                }
                catch (JSONException e) {e.printStackTrace();}
                catch (IOException e) { e.printStackTrace();}

            }
            scheduleToPlot.setRoute(route);
            return scheduleToPlot;
        }

  
        /**
         * An example helper method to call a web service
         */
        private String makeRoutingCall(String httpRequest) throws MalformedURLException, IOException {
            URL url = new URL(httpRequest);
            HttpURLConnection client = (HttpURLConnection) url.openConnection();
            InputStream in = client.getInputStream();
            BufferedReader br = new BufferedReader(new InputStreamReader(in));
            String returnString = br.readLine();
            client.disconnect();
            return returnString;
        }

        @Override
        protected void onPostExecute(SchedulePlot schedulePlot) {

            // CPSC 210 Students: This method should plot the route onto the map
            // with the given line colour specified in schedulePlot. If there is
            // no route to plot, a dialog box should be displayed.
            if (schedulePlot.getRoute().isEmpty()){
                /*new AlertDialog.Builder(getActivity())
                        .setPositiveButton(R.string.ok, new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface arg0, int arg1) {}
                        }).setTitle("Empty").setMessage("No route to plot!")
                        .show();*/
                createSimpleDialog("No route to plot!").show();
            }
            else{
                // To actually make something show on the map, you can use overlays.
                // For instance, the following code should show a line on a map
                PathOverlay po = createPathOverlay(schedulePlot.getColourOfLine());

                List<GeoPoint> points = schedulePlot.getRoute();
                for (GeoPoint p:points){
                    po.addPoint(p);
                }
                scheduleOverlay.add(po);
                OverlayManager om = mapView.getOverlayManager();
                om.addAll(scheduleOverlay);
                plotBuildings(schedulePlot);
                mapView.invalidate(); // cause map to redraw
                if (points.size() == 1){
                    createSimpleDialog("Only one section on the day.").show();
                }
            }
    
        }

    }

    /**
     * This asynchronous task is responsible for contacting the FourSquare web service
     * to retrieve all places around UBC that have to do with food. It should load
     * any determined places into PlaceFactory and then display a dialog box of how it did
     */
    private class GetPlaces extends AsyncTask<Void, Void, String> {

        protected String doInBackground(Void... params) {

            // CPSC 210 Students: Complete this method to retrieve a string
            // of JSON from FourSquare. Return the string from this method
            //String date = new SimpleDateFormat("YYYY-MM-DD").format(new Date());
            //date.replaceAll("-", "");
            String url = FOUR_SQUARE_URL + "?client_id=" + FOUR_SQUARE_CLIENT_ID + "&client_secret=" +
                    FOUR_SQUARE_CLIENT_SECRET + "&ll=" + String.valueOf(UBC_MARTHA_PIPER_FOUNTAIN.getLatitude())
                    + "," + String.valueOf(UBC_MARTHA_PIPER_FOUNTAIN.getLongitude())+ "&section" +
                    "=food&radius=3800&time=any&day=any&v=" + "20150406" + "&m=foursquare&sortByDistance=1";
            foodType = sharedPreferences.getString("foodTypes", "All");
            try {
                String returned = makeRoutingCall(url);
                return returned;
            } catch (IOException e) {
                e.printStackTrace();
            }
            return null;

        }

        private String makeRoutingCall(String httpRequest) throws MalformedURLException, IOException {
            URL url = new URL(httpRequest);
            HttpURLConnection client = (HttpURLConnection) url.openConnection();
            InputStream in = client.getInputStream();
            BufferedReader br = new BufferedReader(new InputStreamReader(in));
            String returnString = br.readLine();
            client.disconnect();
            return returnString;
        }

        protected void onPostExecute(String jSONOfPlaces) {

            // CPSC 210 Students: Given JSON from FourQuest, parse it and load
            // PlaceFactory
            placeFactory = PlaceFactory.getInstance();
            reviews = new HashMap<LatLon, String>();
            try {
                JSONObject placesJson = new JSONObject(new JSONTokener(jSONOfPlaces));
                JSONArray items = placesJson.getJSONObject("response").getJSONArray("groups")
                        .getJSONObject(0).getJSONArray("items");
                int length = items.length();
                int counter = 0;
                for (int i = 0; i < length; i++){
                    String shortName = items.getJSONObject(i).getJSONObject("venue").getJSONArray("categories")
                            .getJSONObject(0).getString("shortName").toLowerCase();
                    boolean shouldSkip = true;
                    switch(foodType){
                        case "All":
                            shouldSkip = false;
                            break;
                        case "Asian foods":
                            if(shortName.contains("deli")) shouldSkip = false;
                            if(shortName.contains("chinese")) shouldSkip = false;
                            if(shortName.contains("korean")) shouldSkip = false;
                            if(shortName.contains("sushi")) shouldSkip = false;
                            if(shortName.contains("japanese")) shouldSkip = false;
                            if(shortName.contains("indian")) shouldSkip = false;
                            break;
                        case "Western foods":
                            if(shortName.contains("italian")) shouldSkip = false;
                            if(shortName.contains("burger")) shouldSkip = false;
                            if(shortName.contains("pizza")) shouldSkip = false;
                            if(shortName.contains("french")) shouldSkip = false;
                            if(shortName.contains("sandwich")) shouldSkip = false;
                            break;
                        case "Cafes":
                            if(shortName.contains("café")) shouldSkip = false;
                            break;
                        case "Snacks":
                            if(shortName.contains("bakery")) shouldSkip = false;
                            if(shortName.contains("bagel")) shouldSkip = false;
                            if(shortName.contains("tea")) shouldSkip = false;
                            break;
                        case "Vegetarian":
                            if(shortName.contains("vegetarian")) shouldSkip = false;
                            break;
                        case "Others":
                            if(shortName.contains("deli")) break;
                            if(shortName.contains("chinese")) break;
                            if(shortName.contains("korean")) break;
                            if(shortName.contains("sushi")) break;
                            if(shortName.contains("japanese")) break;
                            if(shortName.contains("indian")) break;
                            if(shortName.contains("italian")) break;
                            if(shortName.contains("burger")) break;
                            if(shortName.contains("pizza")) break;
                            if(shortName.contains("french")) break;
                            if(shortName.contains("sandwich")) break;
                            if(shortName.contains("café")) break;
                            if(shortName.contains("bakery")) break;
                            if(shortName.contains("bagel")) break;
                            if(shortName.contains("tea")) break;
                            if(shortName.contains("vegetarian")) break;
                            else shouldSkip = false;
                            break;
                        default:
                            break;
                    }

                    if (shouldSkip) continue; // the following code will be skipped if shouldSkip == true.
                    String review = null;
                    if(items.getJSONObject(i).has("tips"))
                        review = items.getJSONObject(i).getJSONArray("tips").getJSONObject(0).getString("text");

                    String placeName = items.getJSONObject(i).getJSONObject("venue").getString("name");
                    double lat = Double.parseDouble(items.getJSONObject(i).getJSONObject("venue").getJSONObject("location")
                            .getString("lat"));
                    double lon = Double.parseDouble(items.getJSONObject(i).getJSONObject("venue").getJSONObject("location")
                            .getString("lng"));
                    Place place = new Place(placeName, new LatLon(lat, lon));
                    placeFactory.add(place);
                    reviews.put(place.getLatLon(), review);
                    counter++;
                }
                String msg = String.valueOf(counter) + " food places are found to be close to UBC.";
                createSimpleDialog(msg).show();

            } catch (JSONException e) {
                e.printStackTrace();
            }

        }
    }

    /**
     * Initialize the CourseFactory with some courses.
     */
    private void initializeCourses() {
        // CPSC 210 Students: You can change this data if you desire.
        CourseFactory courseFactory = CourseFactory.getInstance();

        Building dmpBuilding = new Building("DMP", new LatLon(49.261474, -123.248060));

        Course cpsc210 = courseFactory.getCourse("CPSC", 210);
        Section aSection = new Section("202", "MWF", "12:00", "12:50", dmpBuilding);
        cpsc210.addSection(aSection);
        aSection.setCourse(cpsc210);
        aSection = new Section("201", "MWF", "16:00", "16:50", dmpBuilding);
        cpsc210.addSection(aSection);
        aSection.setCourse(cpsc210);
        aSection = new Section("BCS", "MWF", "12:00", "12:50", dmpBuilding);
        cpsc210.addSection(aSection);
        aSection.setCourse(cpsc210);

        Course engl222 = courseFactory.getCourse("ENGL", 222);
        aSection = new Section("007", "MWF", "14:00", "14:50", new Building("Buchanan", new LatLon(49.269258, -123.254784)));
        engl222.addSection(aSection);
        aSection.setCourse(engl222);

        Course scie220 = courseFactory.getCourse("SCIE", 220);
        aSection = new Section("200", "MWF", "15:00", "15:50", new Building("Swing", new LatLon(49.262786, -123.255044)));
        scie220.addSection(aSection);
        aSection.setCourse(scie220);

        Course math200 = courseFactory.getCourse("MATH", 200);
        aSection = new Section("201", "MWF", "09:00", "09:50", new Building("Buchanan", new LatLon(49.269258, -123.254784)));
        math200.addSection(aSection);
        aSection.setCourse(math200);

        Course fren102 = courseFactory.getCourse("FREN", 102);
        aSection = new Section("202", "MWF", "11:00", "11:50", new Building("Barber", new LatLon(49.267442,-123.252471)));
        fren102.addSection(aSection);
        aSection.setCourse(fren102);

        Course japn103 = courseFactory.getCourse("JAPN", 103);
        aSection = new Section("002", "MWF", "10:00", "11:50", new Building("Buchanan", new LatLon(49.269258, -123.254784)));
        japn103.addSection(aSection);
        aSection.setCourse(japn103);

        Course scie113 = courseFactory.getCourse("SCIE", 113);
        aSection = new Section("213", "MWF", "13:00", "13:50", new Building("Swing", new LatLon(49.262786, -123.255044)));
        scie113.addSection(aSection);
        aSection.setCourse(scie113);

        Course micb308 = courseFactory.getCourse("MICB", 308);
        aSection = new Section("201", "MWF", "12:00", "12:50", new Building("Woodward", new LatLon(49.264704,-123.247536)));
        micb308.addSection(aSection);
        aSection.setCourse(micb308);

        Course math221 = courseFactory.getCourse("MATH", 221);
        aSection = new Section("202", "TR", "11:00", "12:20", new Building("Klinck", new LatLon(49.266112, -123.254776)));
        math221.addSection(aSection);
        aSection.setCourse(math221);

        Course phys203 = courseFactory.getCourse("PHYS", 203);
        aSection = new Section("201", "TR", "09:30", "10:50", new Building("Hennings", new LatLon(49.266400,-123.252047)));
        phys203.addSection(aSection);
        aSection.setCourse(phys203);

        Course crwr209 = courseFactory.getCourse("CRWR", 209);
        aSection = new Section("002", "TR", "12:30", "13:50", new Building("Geography", new LatLon(49.266039,-123.256129)));
        crwr209.addSection(aSection);
        aSection.setCourse(crwr209);

        Course fnh330 = courseFactory.getCourse("FNH", 330);
        aSection = new Section("002", "TR", "15:00", "16:20", new Building("MacMillian", new LatLon(49.261167,-123.251157)));
        fnh330.addSection(aSection);
        aSection.setCourse(fnh330);

        Course cpsc499 = courseFactory.getCourse("CPSC", 430);
        aSection = new Section("201", "TR", "16:20", "17:50", new Building("Liu", new LatLon(49.267632,-123.259334)));
        cpsc499.addSection(aSection);
        aSection.setCourse(cpsc499);

        Course chem250 = courseFactory.getCourse("CHEM", 250);
        aSection = new Section("203", "TR", "10:00", "11:20", new Building("Klinck", new LatLon(49.266112, -123.254776)));
        chem250.addSection(aSection);
        aSection.setCourse(chem250);

        Course eosc222 = courseFactory.getCourse("EOSC", 222);
        aSection = new Section("200", "TR", "11:00", "12:20", new Building("ESB", new LatLon(49.262866, -123.25323)));
        eosc222.addSection(aSection);
        aSection.setCourse(eosc222);

        Course biol201 = courseFactory.getCourse("BIOL", 201);
        aSection = new Section("201", "TR", "14:00", "15:20", new Building("BioSci", new LatLon(49.263920, -123.251552)));
        biol201.addSection(aSection);
        aSection.setCourse(biol201);
    }

}

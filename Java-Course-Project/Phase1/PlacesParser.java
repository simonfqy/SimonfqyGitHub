package ca.ubc.cs.cpsc210.meetup.parser;

import java.io.Reader;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONTokener;
import ca.ubc.cs.cpsc210.meetup.model.EatingPlace;
import ca.ubc.cs.cpsc210.meetup.model.PlaceFactory;
import ca.ubc.cs.cpsc210.meetup.util.LatLon;

/**
 * Foursquare location result parse (JSON)
 */
public class PlacesParser {

	/**
	 * Parse JSON from Foursquare output stored into a file
	 * REQUIRES: input is a file with valid data
	 * EFFECTS: parsed data is put into PlaceFactory
	 */
	public void parse(Reader input) {
		// TODO: Complete the implementation of this method. Handle any
		// exceptions by printing out the stack trace
		try{
			JSONObject start = new JSONObject(new JSONTokener(input));
			JSONArray venues = start.getJSONObject("response").getJSONArray("venues");
			int size = venues.length();
			String name = null;
			double lat = 0.0;
			double lon = 0.0;
			for(int i = 0; i < size; i++){
				JSONObject target = venues.getJSONObject(i);
				name = target.getString("name");
				lat = target.getJSONObject("location").getDouble("lat");
				lon = target.getJSONObject("location").getDouble("lng");
				LatLon latlon = new LatLon(lat, lon);
				EatingPlace eatingPlace = new EatingPlace(name, latlon);
				PlaceFactory.getInstance().add(eatingPlace);
			}
		}
		catch(JSONException e){			
		}
		
		
	}

}

package ca.ubc.cs.cpsc210.meetup.model;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * Provide a factory for places that have been "seen"
 */
public class PlaceFactory {
	
	private Map<String, Set<Place>> places;
	private static PlaceFactory instance = null;
	
	/**
	 * A method for returning a PlaceFactory type object, which is the only way to do so.
	 * Singleton pattern is involved.
	 * Effect: returning an instance of PlaceFactory.
	 */
	public static PlaceFactory getInstance(){
		if (instance==null)
			instance = new PlaceFactory();
		return instance;
	}
	
	/**
	 * Resetting the content of instance to null.
	 */
	public static void reset(){
		instance = null;
	}
	
	/**
	 * Constructor. Only the singleton method needs to create.
	 */
	protected PlaceFactory(){
		places = new HashMap<String, Set<Place>>();
	}

	
	// NOTE: A place may not have a unique name. The combination
	// of name, lat and lon is unique.
	
	/**
	 * A method to add a place into the fields of PlaceFactory.
	 * Requires: p is a valid Place object.
	 * Modifies: this
	 * Effects: if the name of p already exists, p is added to the set with that name; otherwise
	 * a new set is created and p is put there.
	 * @param p place of type Place.
	 */
	public void add(Place p){
		if (places.containsKey(p.getName())){
			Set<Place> placesWithName = places.get(p.getName());
			placesWithName.add(p);
		}
		else{
			Set<Place> placeWithName = new HashSet<Place>();
			placeWithName.add(p);
			places.put(p.getName(), placeWithName);
		}
	}
	
	/**
	 * A getter method which returns a set of place that has the same name as supplied
	 * in the parameter.
	 * Requires: name is a valid name for places.
	 * Modifies: this
	 * Effects: if there exists a set of courses with the key being the name supplied,
	 * return that set of courses; otherwise return null.
	 * @param name of type String.
	 * @return
	 */
	public Set<Place> get(String name){
		Set<Place> placesWithName = places.get(name);
		return placesWithName;		
	}

}

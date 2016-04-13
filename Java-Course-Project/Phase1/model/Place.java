package ca.ubc.cs.cpsc210.meetup.model;


import java.util.HashSet;
import java.util.Set;

import ca.ubc.cs.cpsc210.meetup.util.LatLon;

/**
 * A class for place, extending Location class. It has new fields like name and tag
 * compared to Location.
 */
public class Place extends Location {
    
	private String name;
	private Set<String> tag;
	
	/**
	 * Constructor.
	 * @param name
	 * @param latlon
	 */
	public Place(String name, LatLon latlon) {
		super(latlon);
		this.name = name;
		tag = new HashSet<String>();
	}
	
	/**
	 * Constructor when latlon is unspecified.
	 * @param name
	 */
	public Place(String name){
		super(null);
		this.name = name;
	}
	
	/**
	 * Adds the tag to this Place object.
	 * @param tag
	 */
	public void addTag(String tag){
		this.tag.add(tag);
	}
	
	/**
	 * a method examining whether the tag is contained in this Place object.
	 * @param tag A String variable
	 * @return whether this object contains the tag
	 * supplied as the parameter.
	 */
	public boolean containsTag(String tag){
		return (this.tag.contains(tag));
	}
	
	public String getName(){
		return this.name;
	}

}

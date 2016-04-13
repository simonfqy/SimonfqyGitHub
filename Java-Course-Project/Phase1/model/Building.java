package ca.ubc.cs.cpsc210.meetup.model;

import ca.ubc.cs.cpsc210.meetup.util.LatLon;

/**
 * A class for building, extending Location. Buildings have names, which is absent in
 * Location.
 *
 */
public class Building extends Location {
	
	private String name;

	public Building(String name, LatLon latlon) {
		super(latlon);
		this.name = name;
	}
	
	/**
	 * Constructor with only name of building specified.
	 * @param name name of the building.
	 */
	public Building(String name){
		super(null);
		this.name = name;
	}

}

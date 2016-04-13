package ca.ubc.cs.cpsc210.meetup.model;

import ca.ubc.cs.cpsc210.meetup.util.LatLon;

/**
 * A class for location. Has fields latlon and displayText.
 *
 */
public abstract class Location {
    
	private LatLon latlon;
	private String displayText;
	
	/**
	 * Constructor.
	 * @param latlon the position coordinates of the location.
	 */
	public Location(LatLon latlon) {
		this.latlon = latlon;
	}
	
	public int hashCode() {
		return (latlon.hashCode());
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Location other = (Location) obj;
		if (! latlon.equals(other.latlon))
			return false;
		return true;
	}

}

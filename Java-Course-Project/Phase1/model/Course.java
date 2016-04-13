package ca.ubc.cs.cpsc210.meetup.model;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

import ca.ubc.cs.cpsc210.meetup.util.LatLon;

/**
 * A class for Course, includes code, number and a set for sections, which
 * may be null at the beginning.
 */
public class Course {
	
	private String code;
	private int number;
	private Set<Section> sections;
	
	/**
	 * Constructor. Initialize the course code and number,
	 * as well as creating a new sections list with no elements.
	 * @param code  The string of the courses' offering department.
	 * @param number The number for the course, often in 3 digits. 
	 */
	public Course(String code, int number) {
		this.code = code;
		this.number = number;
		this.sections = new HashSet<Section>();
	}
	
	/**
	 * Adding a section to the set sections.
	 * Modifies: this, section
	 * Effects: the set sections of this object now contain the parameter;
	 * the parameter's course field is also set to this object.
	 */
	public void addSection(Section section){
		sections.add(section);
		section.setCourse(this);
	}

	public int getNumber() {
		return this.number;
	}

	public Section getSection(String sectionId) {
		for (Section sec:sections){
			if (sec.getSectionId().equals(sectionId))
				return sec;
		}
		return null;
	}
	
	public String getCode(){
		return code;
	}
	
	public int hashCode() {
		final int prime1 = 53;
		final int prime2 = 79;
		final int prime3 = 73;
		int result = 0;
		int length = code.length();
		for (int i=0; i<length; i++){
			result = result + code.charAt(i) - '0';
		}
		result = (prime1*result + prime2*number + prime3*sections.hashCode())%100000;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Course other = (Course) obj;
		if (!code.equalsIgnoreCase(other.code))
			return false;
		if (number != other.number)
			return false;
		if (!sections.equals(other.sections))
			return false;
		return true;
	}

}

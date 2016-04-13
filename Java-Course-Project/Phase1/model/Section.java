package ca.ubc.cs.cpsc210.meetup.model;

import ca.ubc.cs.cpsc210.meetup.exceptions.IllegalCourseTimeException;
import ca.ubc.cs.cpsc210.meetup.exceptions.IllegalSectionInitialization;
import ca.ubc.cs.cpsc210.meetup.util.CourseTime;


/**
 * Represent a section for a course
 */
public class Section implements Comparable<Section> {

	private String name;
	private String day;
	private Building building;
	private Course course;
	private String sectionId;
	
	// Time of course is provided to implement comparable
	private CourseTime timeOfCourse;

	/**
	 * Constructor 
	 * REQUIRES: name is not null, day is "MWF" or "TR", startTime
	 *   is before endTime and building is not null 
	 * EFFECTS: object is initialized
	 *   or the exception IllegalSectionInitialization has occurred
	 */
	public Section(String name, String day, String startTime, String endTime,
			Building building){
		CourseTime start, end;
		try{
		try {
			start = new CourseTime(startTime, "23:59");
			end = new CourseTime(endTime, "23:59");
		} catch (IllegalCourseTimeException e) {
			throw new IllegalSectionInitialization("Invalid construction of Section");	
		}
		if (name != null && (day == "MWF" || day =="TR") && start.compareTo(end) < 0 &&
				building != null){
			this.name = name; 
			this.day = day;
			try {
				timeOfCourse = new CourseTime(startTime, endTime);
			} catch (IllegalCourseTimeException e) {
			}
			this.building = building;
			setCourse(new Course("AAAA", 000));
			sectionId = name;
		}
		else
			throw new IllegalSectionInitialization("Invalid construction of Section");
		}
		catch(IllegalSectionInitialization e){			
		}
		
	}

	
	/**
	 * Sets the course field of this object.
	 * @param course
	 */
	public void setCourse(Course course){
		this.course = course;
	}
	
	public void setDay(String day){
		this.day = day;
	}
	
	public void setTime(CourseTime time){
		timeOfCourse = time;
	}
	
	public void setBuilding(Building building){
		this.building = building;
	}

	@Override
	public int compareTo(Section o) {
		return timeOfCourse.compareTo(o.timeOfCourse);
	}
    /**
     * Getter method, getting the day field of this object.
     * @return String day
     */
	public String getday() {
		return this.day;
	}
	
	/**
	 * Getter method, getting the course field of this object.
	 * @return course
	 */
	public Course getcourse(){
		return this.course;
	}
	
	/**
	 * Getter method, getting the timeOfCourse field of this object.
	 * @return timeOfCourse
	 */
	public CourseTime getTime(){
		return this.timeOfCourse;
	}
	
	public String getSectionId(){
		return this.sectionId;
	}
	
	public Building getBuilding(){
		return this.building;
	}
	
	public int hashCode() {
		final int prime1 = 97;
		final int prime2 = 89;
		final int prime3 = 83;
		int result;
		result = (prime1*sectionId.hashCode() + prime2*day.hashCode() + prime3*building.hashCode())%100000;
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
		Section other = (Section) obj;
		if (!day.equalsIgnoreCase(other.day))
			return false;
		if (!timeOfCourse.equals(other.timeOfCourse))
			return false;
		if (!course.getCode().equals(other.course.getCode()))
			return false;
		if (course.getNumber() != other.course.getNumber())
			return false;
		if (!sectionId.equals(other.sectionId))
			return false;
		if (!building.equals(other.building))
			return false;		
		return true;
	}

}

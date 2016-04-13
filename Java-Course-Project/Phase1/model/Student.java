package ca.ubc.cs.cpsc210.meetup.model;

import ca.ubc.cs.cpsc210.meetup.util.CourseTime;

/**
 * A class created to represent students.
 *
 */
public class Student {
	private String firstName;
    private String lastName;
	private int id;
	private Schedule sched;
    
	/**
	 * Create a new Student object according to the input parameters.
	 * @param lastName
	 * @param firstName
	 * @param id
	 */
	public Student(String lastName, String firstName, int id) {
		this.lastName = lastName;
		this.firstName = firstName;
		this.id = id;
	}
	
	/**
	 * A setter method, setting the Student object's sched field as
	 * the input parameter schedule.
	 * @param schedule
	 */
	public void setSchedule(Schedule schedule){
		this.sched = schedule;
	}
    
	/**
	 * A getter method, retrieving the student's schedule.
	 * @return sched
	 */
	public Schedule getSchedule() {
		if (sched == null)
			sched = new Schedule();
		return this.sched;
	}

	public String getLastName() {
		return lastName;
	}

	public Object getFirstName() {
		return firstName;
	}
	
	public int hashCode() {
		final int prime = 53;
		int result;
		result = (prime*id)%50000;
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
		Student other = (Student) obj;
		if (id != other.id)
			return false;
		return true;
	}

}

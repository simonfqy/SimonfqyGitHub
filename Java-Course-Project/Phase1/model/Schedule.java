package ca.ubc.cs.cpsc210.meetup.model;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;

import ca.ubc.cs.cpsc210.meetup.exceptions.IllegalCourseTimeException;
import ca.ubc.cs.cpsc210.meetup.exceptions.IllegalSectionInitialization;
import ca.ubc.cs.cpsc210.meetup.util.CourseTime;

/**
 * Represent a student's schedule consisting of all sections they must attend
 */
public class Schedule {

	private SortedSet<Section> MWFsections;
	private SortedSet<Section> TRsections;

	/**
	 * Constructor
	 */
	public Schedule() {
		MWFsections = new TreeSet<Section>();
		TRsections = new TreeSet<Section>();
	}

	/**
	 * Add a section to the student's schedule 
	 * REQUIRES: section is not null
	 * MODIFIES: this 
	 * EFFECTS: if section is not well-formed, throws
	 * IllegalSectionInitialization otherwise, section is remembered in the
	 * schedule
	 */
	public void add(Section section){
		try{
		if (section == null || section.getcourse() == null) throw new IllegalSectionInitialization("The section is null.");
		if (section.getday().equalsIgnoreCase("MWF"))
			MWFsections.add(section);
		if (section.getday().equalsIgnoreCase("TR"))
			TRsections.add(section);
		}
		catch(IllegalSectionInitialization e){
		}
	}

	/**
	 * Retrieve the earliest start time in the schedule on a given day 
	 * REQUIRES: dayOfWeek is either "MWF" or "TR" 
	 * EFFECTS: Returns the start and end
	 *    times of the earliest section on that day or null
	 */
	public CourseTime startTime(String dayOfWeek) {
		if (dayOfWeek.equalsIgnoreCase("MWF"))
			return (MWFsections.first().getTime());
		if (dayOfWeek.equalsIgnoreCase("TR"))
			return (TRsections.first().getTime());
		else return null;
	}

	/**
	 * Retrieve the latest start time in the schedule on a given day 
	 * REQUIRES: dayOfWeek is either "MWF" or "TR" 
	 * EFFECTS: Returns the start and end
	 *    times of the latest section on that day or null
	 */
	public CourseTime endTime(String dayOfWeek) {
		if (dayOfWeek.equalsIgnoreCase("MWF"))
			return (MWFsections.last().getTime());
		if (dayOfWeek.equalsIgnoreCase("TR"))
			return (TRsections.last().getTime());
		return null;
	}

	/**
	 * Find the start time of all two hour breaks less than the end time
	 * REQUIRES: dayOfWeek is either "MWF" or "TR" 
	 * EFFECTS: Returns a set of the end time before any 2 hour break. The end time is in HH:MM format.
	 */
	public Set<String> getStartTimesOfBreaks(String dayOfWeek) {
		SortedSet<Section> workSet;
		Set<String> result = new HashSet<String>();
		if (dayOfWeek.equalsIgnoreCase("MWF")) workSet = MWFsections;
		else if (dayOfWeek.equalsIgnoreCase("TR")) workSet = TRsections;
		else workSet = null;
		Iterator<Section> itr = workSet.iterator();
		if (!itr.hasNext()) {
			result.add("00:00");
			return result;   // if there are no courses on the day, return the first minute of the day.
		}
		Section previous = itr.next();
		do{
			if (!itr.hasNext()){
				result.add(previous.getTime().getEndTime());
				break;
			}
			Section next = itr.next();
			int indexOfColon = previous.getTime().getEndTime().indexOf(":");
			int length = previous.getTime().getEndTime().length();
			int preEndHour = Integer.parseInt(previous.getTime().getEndTime().substring(0, indexOfColon));
			int preEndMin = Integer.parseInt(previous.getTime().getEndTime().substring(indexOfColon + 1, length));
			indexOfColon = next.getTime().getStartTime().indexOf(":");
			length = next.getTime().getStartTime().length();
			int nextStartHour = Integer.parseInt(next.getTime().getStartTime().substring(0,indexOfColon));
			int nextStartMin = Integer.parseInt(next.getTime().getStartTime().substring(indexOfColon + 1, length));
			if (nextStartHour-preEndHour>2){
				String startBreak = previous.getTime().getEndTime();
				result.add(startBreak);
			}
			else if(nextStartHour-preEndHour==2 && nextStartMin >= preEndMin){
				String startBreak = previous.getTime().getEndTime();
				result.add(startBreak);
			}
			if (!itr.hasNext()) break;
			previous = next;
		}while(true);
		return result;
	}

	/**
	 * In which building was I before the given timeOfDay on the given dayOfWeek
	 * REQUIRES: dayOfWeek is "MWF or "TR" and timeOfDay is non-null and of
	 * format HH:MM 
	 * EFFECTS: The Building in which the student last was before
	 * timeOfDay on dayOfWeek or null
	 */
	public Building whereAmI(String dayOfWeek, String timeOfDay) {
		try{
		SortedSet<Section> workSet;
	    if (dayOfWeek.equalsIgnoreCase("MWF")) workSet = MWFsections;
	    else if (dayOfWeek.equalsIgnoreCase("TR")) workSet = TRsections;
	    else return null;   // input is invalid. No need to proceed.
	    if (workSet.isEmpty()) return null;  // no classes on this dayOfWeek. Return null.
	    CourseTime query = new CourseTime(timeOfDay, "23:59");  // query represents the input time.
	    Iterator<Section> itr = workSet.iterator();
		Section previous = itr.next();
		do{
			CourseTime pre = new CourseTime(previous.getTime().getStartTime(), "23:59");
			if (query.compareTo(pre) < 0) return null; // before the time asked, there were no sections on the day.
			if (itr.hasNext()){
				Section next = itr.next();
				CourseTime successor = new CourseTime(next.getTime().getStartTime(), "23:59");
				if (query.compareTo(pre) >= 0 && query.compareTo(successor) < 0) break;
				previous = next;
			}
			else break; // If the previous section starts earlier than the time we ask and there are no 
			                                    // sections after the previous one, we return the building of previous section.				
		}while(true);
		return previous.getBuilding();
		}catch(IllegalCourseTimeException e){	
			
		}
		return null;
	    
	}


}

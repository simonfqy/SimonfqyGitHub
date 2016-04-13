package ca.ubc.cs.cpsc210.meetup.parser;

import java.util.HashSet;
import java.util.Locale;
import java.util.Set;

import org.xml.sax.Attributes;
import org.xml.sax.helpers.DefaultHandler;

import ca.ubc.cs.cpsc210.meetup.exceptions.IllegalStudentException;
import ca.ubc.cs.cpsc210.meetup.model.Section;
import ca.ubc.cs.cpsc210.meetup.model.Student;
import ca.ubc.cs.cpsc210.meetup.model.StudentManager;

/**
 * Parse XML of a schedule (Sax parser)
 */

public class ScheduleParser extends DefaultHandler {

	private StringBuffer accumulator;
	private String firstName;
	private String lastName;
	private int id;
	private int sid;
	private StudentManager manager;
	private String name;
	private String courseCode;
	private String courseNumber;

	public ScheduleParser(StudentManager manager) {
		this.manager = manager;
	}

	/**
	 * Called at the start of the document (as the name suggests)
	 */
	@Override
	public void startDocument() {
		System.out.println("Start Document!");
		accumulator = new StringBuffer();
		firstName = null;
		lastName = null;
		id = 0;
		sid = 0;
		name = null;
		courseCode = null;
		courseNumber = null;
	}

	/**
	 * Called when the parsing of an element starts. (e.g., <book>)
	 * 
	 * Lookup documentation to learn meanings of parameters.
	 */
	@Override
	public void startElement(String namespaceURI, String localName,
			String qName, Attributes atts) {
		System.out.println("StartElement: " + qName);
		if (qName.toLowerCase().equals("schedules")){
			// Its a Schedule! write out the xmlns:i
			System.out.println("xmlns:i = " + atts.getValue("xmlns:i"));
			firstName = null;
			lastName = null;
			id = 0;
			sid = 0;
			name = null;
			courseCode = null;
			courseNumber = null;
		}
		if (qName.toLowerCase().equals("student")){
			lastName = null;
			firstName = null;
			id = 0;
		}
		if (qName.toLowerCase().equals("schedule")){
			sid = 0;
			name = null;
			courseCode = null;
			courseNumber = null;
		}
		if (qName.toLowerCase().equals("section")){
			System.out.println("name = " + atts.getValue(0));
			name = atts.getValue(0);
			System.out.println("courseCode = " + atts.getValue(1));
			courseCode = atts.getValue(1);
			System.out.println("courseNumber = " + atts.getValue(2));
			courseNumber = atts.getValue(2);
			manager.addSectionToSchedule(sid, courseCode, Integer.parseInt(courseNumber), name);
		}
		accumulator.setLength(0);
	}

	/**
	 * Called for values of elements
	 * 
	 * Lookup documentation to learn meanings of parameters.
	 */
	public void characters(char[] temp, int start, int length) {
		// Remember the value parsed
		accumulator.append(temp, start, length);
	}

	/**
	 * Called when the end of an element is seen. (e.g., </title>)
	 * 
	 * Lookup documentation to learn meanings of parameters.
	 */
	public void endElement(String uri, String localName, String qName) {
		// Print out that we have seen the end of an element
		System.out.println("EndElement: " + qName + " value: " + accumulator.toString().trim());
		
		if(qName.toLowerCase().equals("lastname")){
			lastName = accumulator.toString();
			if (lastName.isEmpty()) throw new IllegalStudentException("Last name is empty!");
		}			
		else if(qName.toLowerCase().equals("firstname")){
			firstName = accumulator.toString();
			if (firstName.isEmpty()) throw new IllegalStudentException("First name is empty!");
		}
		else if(qName.toLowerCase().equals("id"))
			id = Integer.parseInt(accumulator.toString());
		
		if(qName.toLowerCase().equals("student")){
			manager.addStudent(lastName, firstName, id);
		}
		
		if (qName.toLowerCase().equals("studentid"))
			sid = Integer.parseInt(accumulator.toString());
		if (qName.toLowerCase().equals("schedule")){			
			sid = 0;
		}		
		accumulator.setLength(0);
	}
	
	public void endDocument() {
		// Just let the user know as something to do
		System.out.println("End Document!");
	}

}

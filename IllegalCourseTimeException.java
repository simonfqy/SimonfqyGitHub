package ca.ubc.cs.cpsc210.meetup.exceptions;

public class IllegalCourseTimeException extends Exception {

	public IllegalCourseTimeException(String message) {
		super(message);
	}

	public IllegalCourseTimeException(Throwable cause) {
		super(cause);
		// TODO Auto-generated constructor stub
	}

	public IllegalCourseTimeException(String message, Throwable cause) {
		super(message, cause);
		// TODO Auto-generated constructor stub
	}

	public IllegalCourseTimeException(String message, Throwable cause,
			boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
		// TODO Auto-generated constructor stub
	}

}

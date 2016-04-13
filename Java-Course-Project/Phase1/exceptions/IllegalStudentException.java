package ca.ubc.cs.cpsc210.meetup.exceptions;

@SuppressWarnings("serial")
public class IllegalStudentException extends RuntimeException {

	public IllegalStudentException() {
		super();
	}

	public IllegalStudentException(String message) {
		super(message);
	}

	public IllegalStudentException(Throwable cause) {
		super(cause);
		// TODO Auto-generated constructor stub
	}

	public IllegalStudentException(String message, Throwable cause) {
		super(message, cause);
		// TODO Auto-generated constructor stub
	}

	public IllegalStudentException(String message, Throwable cause,
			boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
		// TODO Auto-generated constructor stub
	}

}

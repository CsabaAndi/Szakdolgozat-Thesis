class BaseError extends Error {
    constructor(message: string) {
        super(message);  // Call the parent constructor (Error) with the message

        // Set the name property to the class name (useful for debugging)
        this.name = this.constructor.name;

        // This is important to preserve the stack trace when extending Error
        if (Error.captureStackTrace) {
            Error.captureStackTrace(this, this.constructor);
        }
    }
}

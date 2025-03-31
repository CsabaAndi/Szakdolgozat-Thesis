//TODO: Custom Errors
class baseError extends Error {
    constructor(message: string){
        super(message)
        this.name = `baseError`;
    }
}

import { createWriteStream, mkdirSync, existsSync } from "fs";
import { join } from "path";

/**
 * Log error details to a file.
 * The log file is named with the current date, and logs are appended.
 * @param time - The timestamp of the error.
 * @param loopUrl - The URL or reference related to the loop.
 * @param message - The error message.
 * @returns void
 */
export default function logError(time: string, loopUrl: string, message: Error): void {
    // Get the current date for the filename
    const currentDate = new Date().toISOString().split('T')[0]; // e.g., "2025-04-09"
    
    // Define log directory and filename
    const logDir = '../logs/errors';  // Path to the log directory
    const logFile = join(logDir, `logs-${currentDate}.txt`); // Log file named with the current date
    
    // Check if the directory exists, and create it if not
    if (!existsSync(logDir)) {
        mkdirSync(logDir, { recursive: true });
    }

    // Create a write stream for logging (in append mode)
    const stream = createWriteStream(logFile, { flags: 'a' });

    // Format time into a more readable format
    const readableTime = new Date(time).toLocaleString();

    // Function to strip ANSI escape codes from strings
    function stripAnsiCodes(str: string): string {
        // Regex to remove ANSI escape sequences
        return str.replace(/\x1b\[([0-9]{1,2})(;[0-9]{1,2})?[m|K]/g, '');
    }

    // Strip any ANSI codes from the error message and stack trace
    const cleanMessage = stripAnsiCodes(message.message);
    const cleanStack = message.stack ? stripAnsiCodes(message.stack) : 'No stack trace available';

    // Create an error log object with additional details
    const logDetails = `
=========================================
[${readableTime}] - ERROR LOG

URL: ${loopUrl}
Message: ${cleanMessage}
Stack Trace:
${cleanStack}

=========================================
    `;

    // Write the formatted log entry to the file
    stream.write(logDetails, (err) => {
        if (err) {
            console.error("Error writing to log file:", err);
        }
    });

    // Close the stream to ensure proper file writing
    stream.end();
}

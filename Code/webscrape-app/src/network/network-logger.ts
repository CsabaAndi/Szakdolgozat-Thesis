import { appendFileSync, writeFileSync, mkdirSync } from "fs"
import { dirname, resolve } from 'path';
import { Route } from "@playwright/test";

const options: Intl.DateTimeFormatOptions = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    timeZoneName: 'short',
};

// Create a formatted timestamp
const logTimestamp: string = new Date().toLocaleString(undefined, options)
    .replace(/\//g, '-')           // Replace slashes with dashes
    .replace(/,/g, '')             // Remove commas
    .replace(/ /g, '-')            // Replace spaces with dashes
    .replace(/:/g, '-')            // Replace colons with dashes
    .replace(/GMT.*/, '');         // Remove GMT part if not needed

// Define the path to your log file
const logFilePath = `../logs/network/networkLogs-${logTimestamp}.txt`;


function createNetworkLogFile(): void {
    const headerContent = '-------------------- Log Start --------------------\n\n';
    console.log(process.cwd())

    // Resolve the full path to the log file
    const resolvedPath = resolve(logFilePath);
    const dirPath = dirname(resolvedPath);
    mkdirSync(dirPath, { recursive: true });

    writeFileSync(resolvedPath, headerContent, 'utf8');
}

// Function to append to the log file synchronously
function appendLog(content: string, time: string): void{
    try {
        appendFileSync(logFilePath, content, 'utf8'); // Append content to the file
        console.log(`  [LOG] | Current Time: ${time} - [Log appended to file successfully]: ${logFilePath}`);
    } catch (err) {
        console.error(`  [LOG] | Current Time: ${time} - [Error appending log to file]:`, err);
    }
}

// Helper function to generate log content
function generateLogContent(route: Route, currentTime: string, nth: number): string {
    return `---------------------------------------------------------------------------------------------------------
      Time: ${currentTime}
      Nth Request: ${nth}
      Request ID: ${route.request().postData()}
      Request URL: ${route.request().url()}
      Request Method: ${route.request().method()}
      Request Headers: ${JSON.stringify(route.request().headers(), null, 2)}
    ---------------------------------------------------------------------------------------------------------`;
  }


export  { appendLog, createNetworkLogFile, generateLogContent }
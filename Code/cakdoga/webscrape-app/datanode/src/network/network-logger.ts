import { appendFileSync, writeFileSync, existsSync } from "fs"
import { Route } from "@playwright/test";

const options: Intl.DateTimeFormatOptions = {  year: 'numeric',  month: '2-digit',  day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', timeZoneName: 'short' }
const logTimestamp: any = new Date(Date.now()).toLocaleString(undefined, options).replace(/[/, ]/g, '-')
const logFilePath = `../logs/network/networkLogs-${logTimestamp}.txt`; // Define the path to your log file


function createNetworkLogFile(): void {
    const headerContent = '-------------------- Log Start --------------------\n\n';
    writeFileSync(logFilePath, headerContent, 'utf8');
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
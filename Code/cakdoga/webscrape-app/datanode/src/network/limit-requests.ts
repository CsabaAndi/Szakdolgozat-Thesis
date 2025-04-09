import { BrowserContext, Route } from "@playwright/test";
import { setTimeout } from "timers/promises";
import { config } from 'dotenv';
import { appendLog, createNetworkLogFile, generateLogContent } from './network-logger';

config({path: '../.env'})

let requestCounter = 0; // To track requests 
let isRequestInProgress = false;  // To track if a request is already being processed

const options: Intl.DateTimeFormatOptions = { timeZoneName: 'short' }
const currentTime = new Date(Date.now()).toLocaleString(undefined, options);

const RESOURCE_NAME_EXCLUSIONS = process.env.RESOURCE_NAME_EXCLUSIONS?.split(',') || []
const RESOURCE_TYPE_EXCLUSIONS = process.env.RESOURCE_TYPE_EXCLUSIONS?.split(',') || []

/**
 * Function to handle each request with a X second delay.
 * @param perMinute - Number of requests per minute.
 * @returns Promise<void> Resolves when the requests have been handled.
 */
async function rateLimit(perMinute: number): Promise<void> {
  const minute = 60 * 1000; // 1 minute in milliseconds

  if (perMinute <= 0 || perMinute > 7) {
    console.error(`Invalid perMinute value: ${perMinute}. Setting to default value of 1.`);
    perMinute = 1;
  }
  let delay = minute / perMinute; // Calculate delay based on requests per minute

  await setTimeout(delay); // Wait for the calculated delay
}


/**
 * Function to handle each request with a X second delay.
 * @param route - The route object representing the request.
 * @returns Promise<void> Resolves when the requests have been handled.
 * 
 * @see {@link rateLimit()} - Sets a delay between requests to avoid overwhelming the server.
 */
async function limitRequests(route: Route): Promise<void> {
  // Wait until no other request is being processed (sequential execution)
  while (isRequestInProgress) {
    await setTimeout(100);  // Wait for 100ms before checking again
  }
  isRequestInProgress = true;
  
  try {
    requestCounter++;
    let requestURL = route.request().url();
    const logContent = `---------------------------------------------------------------------------------------------------------
      Time: ${currentTime}
      Nth Request: ${requestCounter}
      Request URL: ${requestURL}
      Request Method: ${route.request().method()}
      Request Headers: ${JSON.stringify(route.request().headers(), null, 10)}\n
    ---------------------------------------------------------------------------------------------------------`;
    const shouldAbort = RESOURCE_TYPE_EXCLUSIONS.includes(route.request().resourceType()) // || RESOURCE_NAME_EXCLUSIONS.some(elem => route.request().url().includes(elem)) // nameben van vmi

    if (shouldAbort) {
      await route.abort();
      console.log(`Current Time: ${currentTime} - [Request aborted]: ${requestURL}`);
    } else {
      appendLog(logContent, currentTime);
      await rateLimit(5) // Rate limit to x requests per minute (minimum 7 seconds delay)
      console.log(`[Request] | Nth Request: ${requestCounter}. | Current Time: ${currentTime} - [Request allowed]: ${requestURL}`);
      route.continue();
    }
  } catch (err) {
    console.error(`Current Time: ${currentTime} - [Error processing request]:`, err);
  } finally {
    isRequestInProgress = false;
  }
}


/**
 * Calls limitRequests() for every requests (Rate limits request to x / minute, and blocks unwanted resources.)
 * @param context
 * @returns Promise<void> Resolves when the requests have been handled.
 * 
 * @see {@link limitRequests()} - The function responsible for enforcing the rate limiting and blocking unwanted resources.
 */
async function handleRequests(context: BrowserContext): Promise<void> {
  createNetworkLogFile();
  await context.route('**/*', async (route) => {
    await limitRequests(route);
  });
}


export  { handleRequests }
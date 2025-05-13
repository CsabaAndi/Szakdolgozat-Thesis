/*
Legal Notice

This is for demonstration purposes only. 
The data used complies with the source website's [Terms of Use](https://www.sports-reference.com/termsofuse.html), 
[Data Use](https://www.sports-reference.com/data_use.html) policies, and [traffic/scraper limitations](https://www.sports-reference.com/bot-traffic.html).
No data has been stored in a database, and the scraper has not been used beyond this demo context.
The data has not been used in any way for model training or statistical analysis.

Important Note:
This scraper is non-functional by default and requires manual configuration of environment variables. 
By setting up and using these variables, the user assumes full responsibility for complying with the applicable Terms of Service and legal policies of the target website.
This tool is not intended for active scraping or data collection and is provided solely for demonstration and educational purposes.

*/


import { firefox, devices, chromium, errors} from 'playwright';
import { expect } from '@playwright/test';
import { setTimeout } from "timers/promises";
import { Command } from 'commander';
import { config } from 'dotenv';
import { handleRequests } from './network/limit-requests';
import logError from './file-io/logger';
//import { getLeagueTableData, getPlayerTableData, getOverUnderTableData, getWideTableData, getMatchHistoryData, getTeamLinks } from './table-parsers';
//import { matchHistory } from './match-history';
//import { readFromJson } from './update'


// TODO: clean imports/exports
// TODO: browser extensions not working currently [browser path starts from appdata instead of persistent data folder in project]

config({path: '../.env'});
const URLS = process.env.URLS?.split(',') || []
const program = new Command();

program
  .option('-p, --page <page>', 'numberic value to turn back pages', parseFloat, 1)
  .option('-l, --loop <loop>', 'bool, loop through all links or just first', false)
  .parse(process.argv);

const options = program.opts();
//const isLoop = options.loop.toLowerCase() === 'true';

/** Main function */
(async () => {
  const start = Date.now();
  let html: string  = ""; // rename ?
  const browserContext = await chromium.launchPersistentContext(process.env.DATA_DIR ?? '', {
    headless: process.env.HEADLESS === 'true',  // Convert the string to a boolean
    userAgent: process.env.USER_AGENT,
    viewport: {
      width: parseInt(process.env.VIEWPORT_WIDTH ?? '1920', 10),  // Convert to integer
      height: parseInt(process.env.VIEWPORT_HEIGHT ?? '1080', 10)  // Convert to integer
    },
    args: process.env.ARGS ? process.env.ARGS.split(',') : [],
  });

  handleRequests(browserContext);
  const firstPage = browserContext.pages()[0]
  for await (const url of URLS){
    console.log("Current URL:", url)
    try{ 
      const x = url.split(`/`)
      console.log(x)

      await firstPage.goto(url, {timeout: 0});
      await setTimeout(5000);
      break;

      //await setTimeout(5000);
      

    } catch(error) { 
      const errorTimestamp = new Date();
      try{
        await firstPage.screenshot({ path: `../logs/errors/playwright/`+`${errorTimestamp}`+`.png`, fullPage: true });
      } catch(err) {
        if(err instanceof Error){logError(`${errorTimestamp}`, url, err)};
        console.log("Error - Log: Problem with taking screenshot", err)
      }
      if( error instanceof errors.TimeoutError){console.log(`${errorTimestamp} - Timeout Error`)};
      if(error instanceof Error){logError(`${errorTimestamp}`, url, error)};
      console.log(`${errorTimestamp} -> Other Error`)
      console.log("Error - Log: ", error)
    }
    
  };
  //TODO: Delete after implementing logger
  console.log(`time: ${((Date.now() - start)/1000).toFixed(5)} - sec`);
  console.log("end");
  
  //await setTimeout(5000);
  //await setTimeout(500000);
  
  await browserContext.close();
  await browserContext.close();
})();

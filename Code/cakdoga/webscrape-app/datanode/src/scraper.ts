import { firefox, devices, chromium, errors} from 'playwright';
import { expect } from '@playwright/test';
import { setTimeout } from "timers/promises";
import { handleRequests } from './network/limit-requests';
import { URLS_2023_2024 } from './constans/links';
import { BROWSER_CONFIG } from './constans/browser.config'
import { getLeagueTableData, getPlayerTableData, getOverUnderTableData, getWideTableData, getMatchHistoryData, getTeamLinks } from './table-parsers';
import { matchHistory } from './match-history';
import { readFromJson } from './update'
import { Command } from 'commander';


// TODO: clean imports/exports
// TODO: browser extensions not working currently [browser path starts from appdata instead of persistent data folder in project]


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
  const browserContext = await chromium.launchPersistentContext(BROWSER_CONFIG.dataDir, {
    headless: BROWSER_CONFIG.headless, userAgent: BROWSER_CONFIG.userAgent, viewport: BROWSER_CONFIG.viewport, 
    args: BROWSER_CONFIG.args,
  });

  //requestResourceBlocking(browserContext);
  //limitRequests(browserContext);
  const firstPage = browserContext.pages()[0]
  for await (const url of URLS_2023_2024){
    console.log(url)
    handleRequests(browserContext);
    try{ 
      const x = url.split(`/`)
      console.log(x)

      await firstPage.goto(url, {timeout: 0});
      await setTimeout(5000);
      break;


      //await setTimeout(5000);
      

    } catch(error) { 
      try{
        await firstPage.screenshot({ path: `../logs/errors/playwright`+`${new Date()}`+`-error.png`, fullPage: true });
      } catch(err) {
        console.log("Error - Log: Problem with taking screenshot", err)
      }
      if( error instanceof errors.TimeoutError){console.log(`${new Date()} - Timeout Error`)}
      console.log(`${new Date()} -> Other Error`)
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

import { firefox, devices, chromium, errors} from 'playwright';
import { expect } from '@playwright/test';
import { setTimeout } from "timers/promises";
import { requestResourceBlocking } from './requests/resource-blocking';
import { URLS_2023_2024 } from './constans/links';
import { BROWSER_CONFIG } from './constans/browser.config'
import { getLeagueTableData, getPlayerTableData, getOverUnderTableData, getWideTableData, getMatchHistoryData, getTeamLinks } from './table-parsers';
import { matchHistory } from './match-history';
import { readFromJson } from './update'


// TODO: clean imports/exports
// TODO: browser extensions not working currently [browser path starts from appdata instead of persistent data folder in project]


/** Main function */
(async () => {
  const start = Date.now();
  let html: string  = ""; // rename ?
  const browserContext = await chromium.launchPersistentContext(BROWSER_CONFIG.dataDir, {
    headless: BROWSER_CONFIG.headless, userAgent: BROWSER_CONFIG.userAgent, viewport: BROWSER_CONFIG.viewport, 
    args: BROWSER_CONFIG.args,
  });

  requestResourceBlocking(browserContext);
  const firstPage = browserContext.pages()[0]
  for await (const url of URLS_2023_2024){
    console.log(url)
    try{ 
      const x = url.split(`/`).slice(4, 6)
      await firstPage.goto(url, {timeout: 0});
      
      // headless mode debug
      // await firstPage.screenshot({ path: 'screenshot.png', fullPage: true });

  
      await expect(firstPage.locator("table.detailed-table")).toBeVisible();
      await firstPage.content().then((x) => { html = x });
      getLeagueTableData(html, x);


      await expect(firstPage.locator("table.playerstats")).toBeVisible();
      await firstPage.content().then((x) => { html = x });
      getPlayerTableData(html, x);

      
      await firstPage.getByRole("listitem").filter({hasText: "Over/under"}).click();
      await expect(firstPage.locator("table.overundertable")).toBeVisible();
      await firstPage.content().then((x) => { html = x });
      getOverUnderTableData(html, x);


      await firstPage.getByRole("listitem").filter({hasText: "Wide"}).click();
      await expect(firstPage.locator("table.detailed-table.fixed-wide-table")).toBeVisible();
      await firstPage.content().then((x) => { html = x });
      getWideTableData(html, x);
      
      await matchHistory(browserContext, html, "base");

      //readFromJson()
      
      break;
      
    //TODO
    } catch(error) { 

      await firstPage.screenshot({ path: `../output/dev/logs/errors/`+`${new Date()}`+`-error.png`, fullPage: true });
      if( error instanceof errors.TimeoutError){console.log(`${new Date()} - Timeout Error`)}
      console.log(`${new Date()} -> Other Error`)
      console.log(error)
    }
    
  };
  //TODO: Delete after implementing logger
  console.log(`time: ${((Date.now() - start)/1000).toFixed(5)} - sec`);
  console.log("end");
  
  await setTimeout(5000);
  //await setTimeout(500000);
  
  await browserContext.close();
  await browserContext.close();
})();

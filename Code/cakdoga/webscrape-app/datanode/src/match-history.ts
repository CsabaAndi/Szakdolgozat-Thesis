import { BrowserContext, expect } from '@playwright/test';
import { getMatchHistoryData, getTeamLinks } from './table-parsers';
import { emptyArrays } from './table-parsers';


//TODO: Error Handling
/**
 * Does something
 * @param context - Browser
 * @param html - whole page html
 * @returns Does not return anything
 */
async function matchHistory(context: BrowserContext, html: string, mode:string = "base") {
    const NON_BREAKING_SPACE = String.fromCharCode(160)
    const TURN_BACK_PAGES = 2
    const newPage = await context.newPage();
    /** For checking if new table page data loaded */
    let locatorValue: string;
    /** counter for table page navigation */
    let counter = 0;

    for await (const teamLink of getTeamLinks(html)){
      await newPage.goto(`https://int.soccerway.com${teamLink}matches/`, {timeout: 10000}) 
      const x = teamLink.split(`/`).slice(2, 4)
      await expect(newPage.locator("table.matches")).toBeVisible({timeout: 10000});
      const prevButton = newPage.locator(`span.nav_description`).filter({hasText: `Previous`})
      locatorValue = await newPage.locator(`table.matches > tbody > tr:nth-child(1) > td:nth-child(1)`).innerText({timeout: 10000}) 

      do {
        await newPage.content().then((x) => { html = x });
        getMatchHistoryData(html)

        // NEED TO IMPLEMENT
        if ( mode === "update" ) { break; }

        if ( (locatorValue == NON_BREAKING_SPACE) || (locatorValue == "") || (locatorValue == " ")){ break } 

        if ( await prevButton.isEnabled() && (counter < (TURN_BACK_PAGES-1))){ 
            await prevButton.click() 
            await expect(newPage.locator(`table.matches > tbody > tr:nth-child(1) > td:nth-child(1)`)).not.toContainText(locatorValue, {timeout: 10000}) 
            locatorValue = await newPage.locator(`table.matches > tbody > tr:nth-child(1) > td:nth-child(1)`).innerText() 
        }
        counter++

      }while(counter < TURN_BACK_PAGES);
      counter = 0;
      emptyArrays(x)

    }
    await newPage.close()
  }


  export { matchHistory }
import * as cheerio from 'cheerio';
import { readFile } from "fs"



// TODO: Placeholder implementation 
/**
 * tmp
 * @param  - Path to file output directory
 * @param  - Data to write into json file
 * @returns  Does not return anything
 */
function readFromJson(): void {


  // read team match history json file
  readFile("../output/data/preprocessed/match-history/england/chelsea-football-club.json", 'utf8', (error, data) => { if(error){console.log(error)}; console.log(JSON.parse(data)); return; })  

}



// NEED TO IMPLEMENT  | above readjson
function readMatchHistory(file: void): void {
    // read match history as dataframe

    // return dataframe
};

function writeUpdatedMH(file: void): void {
    // write or update base file
}

function compareAndUpdate(dataframe: void): void {
    // read team match history json file
    // get actual match history data
    // convert actual data to json format
    // compare older data with actual json data
    // if there are new data then
    // update base file with new match history data
}


function emptyArrays(urlPart: string[]): void {
    // writeToJson(`data/match-history/${urlPart[0]}/${urlPart[1]}.json`, matchHistoryTableData);
    // matchHistoryTableData.length = 0 
};




function getMatchHistoryData(pageHtml: string): void {
    const keys: string[] = [`Date`, `League`, `Team_X`, `Score`, `Team_Y`]
    const $ = cheerio.load(pageHtml)
    const $table = $("table.matches > tbody > tr")
    $table.each((rowIndex, row) => {
      let rowData: any = {}
      $(row).find("td").slice(0, 5).each((colIndex, cell) => {
        if (colIndex == 2 || colIndex == 4){
          rowData[`${keys[colIndex]}`] = $(cell).text().trim(); 
          return;
        }
        if (colIndex == 3){rowData[`${keys[colIndex]}`] = $(cell).text().replace(/\n/g, '').replace(/\s+/g, '').trim(); return;}
        rowData[`${keys[colIndex]}`] = $(cell).text().trim();
      });

      // convert data to dataframe
      // matchHistoryTableData.push(rowData)
      rowData = null
    })
    // TODO: write to json 
    //console.log(matchHistoryTableData)
  }


  export { readFromJson }
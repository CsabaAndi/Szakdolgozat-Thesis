import * as cheerio from 'cheerio';
import { LeagueTableRow, LastFiveRow, TopPlayerRow, OverUnderRow, WideRow } from './classes/table-data';
import writeToJson from './file-io/json-writer';


/* TODO: 
// documentation
// Currently `Rank` value gets added as string instead of number 
// Clean code: types, variable names
*/

const matchHistoryTableData: any = [];


/**
 * Does something
 * @param pageHtml - whole page html
 * @param urlPart - Country and League type
 * @returns Does not return anything
 */
function getLeagueTableData(pageHtml: string, urlPart: string[]): any {
  const indexes = Object.keys(new LastFiveRow)
  console.log(indexes)
  const tableData: LastFiveRow[] = [];
  const $ = cheerio.load(pageHtml)
  const $table = $("table.detailed-table > tbody > tr")
  $table.each((rowIndex, row) => {
    let rowData: LastFiveRow = new LastFiveRow()
    $(row).find("td").each((colIndex, cell) => {
      /** Table has more cols than defined in the LastFiveRow class */
      switch (colIndex){
        case 0:
          rowData[indexes[0]] = $(cell).text().trim()
          return;
        case 2:
          rowData[indexes[1]] = ($(row).find("td.large-link > a").attr("title")!).trim()
          return;
        case 11:
          rowData[indexes[2]] = $(row).find("td.form").contents().text().replace(/\s+/g, '').trim()
          return;
      }
    });
    tableData.push(rowData)
  })
  console.log(tableData)
  writeToJson(`data/preprocessed/tables/${urlPart[0]}/${urlPart[1]}/LastFive.json`, tableData);
}


/**
 * Does something
 * @param pageHtml - whole page html
 * * @param urlPart - Country and League type
 * @returns Does not return anything
 */

function getPlayerTableData(pageHtml: string, urlPart: string[]): void {
  const indexes = Object.keys(new TopPlayerRow)
  //const keys: string[] = [`PlayerName`, `TeamName`, `Goals`, `Penalties`, `FirstGoals`]
  const tableData: TopPlayerRow[] = [];

  const $ = cheerio.load(pageHtml)
  const $table = $("table.playerstats > tbody > tr")

  $table.each((rowIndex, row) => {
    let rowData: TopPlayerRow = new TopPlayerRow()
    $(row).find("td").each((colIndex, cell) => {
      if (colIndex == 1){rowData[indexes[colIndex]] = ($(cell).find("a").attr("title")!).trim(); return;}
      rowData[indexes[colIndex]] = $(cell).text().trim();
  });
    tableData.push(rowData)
  })
  console.log(tableData)
  writeToJson(`data/preprocessed/tables/${urlPart[0]}/${urlPart[1]}/Player.json`, tableData);
}


/**
 * Does something
 * @param pageHtml - whole page html
 * @param urlPart - Country and League type
 * @returns Does not return anything
 */
function getOverUnderTableData(pageHtml: string, urlPart: string[]): void {
  const indexes = Object.keys(new OverUnderRow)
  //const keys: string[] = [`Rank`, `TeamName`, `MatchesPlayed`, `Goals_0`, `Goals_1`, `Goals_2`, `Goals_3`, `Goals_4`, `Goals_5`, `Goals_6`, `Goals_7`, `GoalsOver_7`, `Avg`]
  const tableData: OverUnderRow[] = [];

  const $ = cheerio.load(pageHtml)
  const $table = $("table.overundertable > tbody > tr")

  $table.each((rowIndex, row) => {
    let rowData: OverUnderRow = new OverUnderRow()
    $(row).find("td").each((colIndex, cell) => {
      rowData[indexes[colIndex]] = $(cell).text().trim();
    });
    tableData.push(rowData)
  })
  console.log(tableData)
  writeToJson(`data/preprocessed/tables/${urlPart[0]}/${urlPart[1]}/OverUnder.json`, tableData);
}


/**
 * Does something
 * @param pageHtml - whole page html
 * @param urlPart - Country and League type
 * @returns Does not return anything
 */
function getWideTableData(pageHtml: string, urlPart: string[]): void {
  const indexes = Object.keys(new WideRow)
  /*const keys: string[] = [
    `Rank`, `empty_col`, `TeamName`,
    `MatchesPlayed_T`, `Wins_T`, `Draws_T`, `Losses_T`, `GoalsFor_T`, `GoalsAgainst_T`, 
    `MatchesPlayed_H`, `Wins_H`, `Draws_H`, `Losses_H`, `GoalsFor_H`, `GoalsAgainst_H`, 
    `MatchesPlayed_A`, `Wins_A`, `Draws_A`, `Losses_A`, `GoalsFor_A`, `GoalsAgainst_A`, 
    `GoalDifference`, `Points`
  ]*/
  const tableData: WideRow[] = [];

  const $ = cheerio.load(pageHtml)
  const $table = $("table.detailed-table.fixed-wide-table > tbody > tr")

  $table.each((rowIndex, row) => {
    let rowData: WideRow = new WideRow()
    $(row).find("td").each((colIndex, cell) => {
        switch (colIndex){
          case 0:
            rowData[indexes[colIndex]] = $(cell).text().trim();
            break;
          case 2:
            rowData[indexes[colIndex-1]] = ($(cell).find("a").attr("title")!).trim(); 
            break;
          case 1:
            break;
          default:
            rowData[indexes[colIndex-1]] = $(cell).text().trim(); 
        }
    });
    console.log(rowData)
    tableData.push(rowData)
        
  })
  //console.log(tableData)
  writeToJson(`data/preprocessed/tables/${urlPart[0]}/${urlPart[1]}/Wide.json`, tableData);
}

/**
 * Does something
 * @param pageHtml - whole page html 
 * @returns teamLinks an array of strings 
 */
function getTeamLinks(pageHtml: string): string[] {
  const teamLinks: string[] = [];
  const $ = cheerio.load(pageHtml)
  const $table = $("table.detailed-table.fixed-wide-table > tbody > tr")
  $table.each((_, row) => {
    let link: string = $(row).find("td.large-link > a").attr("href")!
    teamLinks.push(link)
  });
  console.log(teamLinks)
  return teamLinks
}

/**
 * Does something
 * @param pageHtml - whole page html
 * @returns Does not return anything
 */
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
    matchHistoryTableData.push(rowData)
    rowData = null
  })
  // TODO: write to json 
  console.log(matchHistoryTableData)
}


/**
 * Calls writeToJson() to write out the data then sets the global array length to 0
 * @returns  Does not return anything
 */
function emptyArrays(urlPart: string[]): void { writeToJson(`data/preprocessed/match-history/${urlPart[0]}/${urlPart[1]}.json`, matchHistoryTableData); matchHistoryTableData.length = 0 }


export { getLeagueTableData, getPlayerTableData, getOverUnderTableData, getWideTableData, getMatchHistoryData, getTeamLinks, emptyArrays }
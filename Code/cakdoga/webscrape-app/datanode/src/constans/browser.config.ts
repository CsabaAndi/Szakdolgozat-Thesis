/** Currently unused */
const CHROME_EXTENSIONS_PATH_UBLOCK = '../browser/browser_extensions/ublock_origin/chromium'

/**
 * BrowserContext properties
 */
const BROWSER_CONFIG = {
    // home linux
    //dataDir: '/home/dct/daily-important/work-study/Szakdolgozat/datanode/browser/browser-data',
    // from src folder
    dataDir: '../browser/browser-data',
    // work win
    //dataDir: 'C:/Users/550008279/OneDrive - GEHealthCare/Desktop/vackok/szakdoga-sajat-cuccok/cakdoga-datanodev0.6.0/cakdoga/webscrape-app/datanode/browser',
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.3',
    viewport: { width: 1920, height: 1080 },
    headless: false,
    args: [
        //`--headless=new` // use this for headless mode
        /*
        `--disable-extensions-except=${CHROME_EXTENSIONS_PATH_UBLOCK}`,
        `--load-extension=${CHROME_EXTENSIONS_PATH_UBLOCK}` 
        */
   ]
};


export { BROWSER_CONFIG };


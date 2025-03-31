import { writeFile, access, mkdir, existsSync, mkdirSync } from "fs"
import * as path from "path"


// TODO: Placeholder implementation 
/**
 * Creates directories recursively if they dont exist, then writes data to file.
 * @param outDir - Path to file output directory
 * @param data - Data to write into json file
 * @returns  Does not return anything
 */
export default function writeToJson(Dir: string, data: any[]): void {
    const outFilePath = path.join(`../output/`, Dir)
    const outDir = path.dirname(outFilePath)

    if(!existsSync(outDir)){ mkdirSync(outDir, {recursive: true}) }
        

    writeFile(outFilePath, JSON.stringify(data), (error) => { if(error){console.log(error); return;} })
}




import { createWriteStream } from "fs"

/**
 * Not Implemented
 * @param time -
 * @param message - 
 * @param loopUrl -
 * @returns 
 */
export default function logError(time: string, loopUrl: string, message: Error): void {
    const stream = createWriteStream(`./../output/logs.txt`, {flags: `a`})
    stream.write(`${JSON.stringify({time, loopUrl, message})}\n`)
}
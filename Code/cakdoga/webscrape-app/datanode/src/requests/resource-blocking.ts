import { BrowserContext } from "@playwright/test";
import { RESOURCE_NAME_EXCLUSIONS, RESOURCE_TYPE_EXCLUSIONS } from '../constans/resources'


/**
 * Filters and blocks out route's request that aren't needed
 * @param context
 * @returns Promise<void>
 */
async function requestResourceBlocking(context: BrowserContext): Promise<void> {
  await context.route('**/*', (route) => {
    return (RESOURCE_TYPE_EXCLUSIONS.includes(route.request().resourceType()) || RESOURCE_NAME_EXCLUSIONS.some(elem => route.request().url().includes(elem)))
      ? route.abort()
      : route.continue();
  });
}


export  {requestResourceBlocking }
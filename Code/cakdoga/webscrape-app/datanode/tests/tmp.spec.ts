
import { test, expect } from '@playwright/test';


test.describe('testing', () => { 
  test(`Testing `, async ({ page }) => {
    await page.goto(`https://youtube.com`)
  });
});

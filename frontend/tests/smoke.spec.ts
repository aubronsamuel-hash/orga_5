import { test, expect } from '@playwright/test'

test('login form visible', async ({ page }) => {
  await page.goto('/')
  await expect(page.getByText('Login')).toBeVisible()
})

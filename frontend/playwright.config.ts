import { defineConfig } from '@playwright/test'

export default defineConfig({
  use: {
    baseURL: 'http://localhost:8080',
    headless: true,
  },
  projects: [{ name: 'chromium', use: { browserName: 'chromium' } }],
})

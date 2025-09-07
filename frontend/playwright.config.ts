import { defineConfig } from '@playwright/test'

export default defineConfig({
  use: {
    baseURL: 'http://localhost:8080',
    headless: true,
  },
  webServer: {
    command: 'npm run build && npm run preview -- --port 8080 --strictPort',
    port: 8080,
    timeout: 120_000,
    reuseExistingServer: !process.env.CI,
  },
  projects: [{ name: 'chromium', use: { browserName: 'chromium' } }],
})

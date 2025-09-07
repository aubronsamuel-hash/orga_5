import { render, screen, waitFor } from '@testing-library/react'
import PlanningView from './planning'

global.fetch = () => Promise.resolve({
  json: () => Promise.resolve([{ id: 1, title: 'A', start_utc: '2025-01-01T10:00:00Z', end_utc: '2025-01-01T11:00:00Z' }])
} as unknown as Response)

test('shows events', async () => {
  render(<PlanningView />)
  await waitFor(() => screen.getByText('A (10:00)'))
})

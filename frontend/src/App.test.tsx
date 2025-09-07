import { render, screen } from '@testing-library/react'
import '@testing-library/jest-dom'
import App from './App'

test('renders hello', () => {
  render(<App />)
  expect(screen.getByText('Hello')).toBeInTheDocument()
})

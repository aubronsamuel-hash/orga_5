import { render, screen } from '@testing-library/react'
import '@testing-library/jest-dom'
import App from './App'
import { AuthProvider } from './auth'

function setup(role: any = null) {
  return render(
    <AuthProvider initialRole={role}>
      <App />
    </AuthProvider>
  )
}

test('admin sees admin area', () => {
  setup('admin')
  expect(screen.getByText('Admin only')).toBeInTheDocument()
})

test('tech does not see admin area', () => {
  setup('tech')
  expect(screen.queryByText('Admin only')).toBeNull()
})

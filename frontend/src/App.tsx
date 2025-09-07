import { useState, FormEvent } from 'react'
import { Button } from './components/ui/button'
import { useAuth, Role } from './auth'
import PlanningView from './planning'

export default function App() {
  const { role, login, logout } = useAuth()
  const [selected, setSelected] = useState<Role>('admin')

  const onSubmit = (e: FormEvent) => {
    e.preventDefault()
    login(selected)
  }

  if (!role) {
    return (
      <form onSubmit={onSubmit} className="p-4 space-y-2">
        <h1 className="text-xl">Login</h1>
        <select value={selected} onChange={e => setSelected(e.target.value as Role)} className="border p-1">
          <option value="admin">admin</option>
          <option value="planner">planner</option>
          <option value="tech">tech</option>
        </select>
        <Button type="submit">Entrer</Button>
      </form>
    )
  }

  if (window.location.pathname === '/planning') {
    return (
      <div className="p-4">
        <PlanningView />
        <Button onClick={logout}>Logout</Button>
      </div>
    )
  }

  return (
    <div className="p-4 space-y-2">
      <h1 className="text-xl">Hello {role}</h1>
      {role === 'admin' && <div>Admin only</div>}
      <Button onClick={logout}>Logout</Button>
    </div>
  )
}

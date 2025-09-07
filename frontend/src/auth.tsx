import { createContext, useContext, useState, ReactNode } from 'react'

export type Role = 'admin' | 'planner' | 'tech'

interface AuthContext {
  role: Role | null
  login: (r: Role) => void
  logout: () => void
}

const Ctx = createContext<AuthContext | undefined>(undefined)

export function AuthProvider({ children, initialRole = null }: { children: ReactNode; initialRole?: Role | null }) {
  const [role, setRole] = useState<Role | null>(initialRole)
  const login = (r: Role) => setRole(r)
  const logout = () => setRole(null)
  return <Ctx.Provider value={{ role, login, logout }}>{children}</Ctx.Provider>
}

export function useAuth() {
  const ctx = useContext(Ctx)
  if (!ctx) throw new Error('AuthProvider missing')
  return ctx
}

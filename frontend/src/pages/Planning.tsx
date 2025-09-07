import { useEffect, useState } from "react";
import { fetchUsers } from "../lib/api";
import Avatar from "../components/Avatar";

type User = { id: number; full_name: string; email: string; avatar_url?: string | null };

export default function Planning() {
  const [users, setUsers] = useState<User[]>([]);
  useEffect(() => {
    fetchUsers().then(setUsers).catch(console.error);
  }, []);

  return (
    <div style={{ display: "grid", gridTemplateColumns: "240px 1fr", height: "100vh" }}>
      <aside style={{ borderRight: "1px solid #eee", padding: 16, overflow: "auto" }}>
        <h2 style={{ fontSize: 18, fontWeight: 700, marginBottom: 12 }}>Employes</h2>
        <div style={{ display: "grid", gap: 8 }}>
          {users.map(u => (
            <div key={u.id} style={{ display: "flex", alignItems: "center", gap: 8 }}>
              <Avatar name={u.full_name} />
              <div>
                <div style={{ fontWeight: 600 }}>{u.full_name}</div>
                <div style={{ fontSize: 12, color: "#666" }}>{u.email}</div>
              </div>
            </div>
          ))}
        </div>
      </aside>
      <main style={{ padding: 16 }}>
        <h1 style={{ fontSize: 20, fontWeight: 700, marginBottom: 12 }}>Planning</h1>
        <div>Zone calendrier a venir.</div>
      </main>
    </div>
  );
}

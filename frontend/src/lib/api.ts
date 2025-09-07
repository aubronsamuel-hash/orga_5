const base = (import.meta as any).env.VITE_API_BASE_URL || "http://localhost:8000";
export async function fetchUsers() {
  const res = await fetch(`${base}/users`);
  if (!res.ok) throw new Error("Failed to load users");
  return res.json();
}

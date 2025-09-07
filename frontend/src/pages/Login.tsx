import { useState } from "react";
import { saveAuth } from "../lib/auth";

const api = (import.meta as any).env.VITE_API_URL || "http://localhost:8000";

export default function Login() {
  const [error, setError] = useState("");

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const form = e.currentTarget;
    const email = (form.elements.namedItem("email") as HTMLInputElement).value;
    const password = (form.elements.namedItem("password") as HTMLInputElement).value;
    const res = await fetch(`${api}/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });
    if (res.ok) {
      const data = await res.json();
      saveAuth(data.access_token, data.user);
      window.location.href = "/planning";
    } else {
      setError("Invalid credentials");
    }
  }

  return (
    <div style={{ display: "grid", placeItems: "center", minHeight: "100vh" }}>
      <form onSubmit={handleSubmit} style={{ width: 320, display: "grid", gap: 12 }}>
        <h1 style={{ fontSize: 24, fontWeight: 700 }}>Login</h1>
        <input name="email" placeholder="Email" required />
        <input name="password" placeholder="Password" type="password" required />
        {error && <div style={{ color: "red" }}>{error}</div>}
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

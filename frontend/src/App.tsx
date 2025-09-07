import { useState } from "react";
import Login from "./pages/Login";
import Planning from "./pages/Planning";

export default function App() {
  const [authed, setAuthed] = useState(false);
  return authed ? <Planning /> : <Login onSuccess={() => setAuthed(true)} />;
}

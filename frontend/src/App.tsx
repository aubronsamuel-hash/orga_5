import { useEffect, useState } from "react";

export default function App() {
  const [status, setStatus] = useState("loading");

  useEffect(() => {
    fetch("/api/health")
      .then((r) => r.json())
      .then((d) => setStatus(d.api))
      .catch(() => setStatus("error"));
  }, []);

  return <div>API health: {status}</div>;
}

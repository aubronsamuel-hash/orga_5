type Props = { onSuccess: () => void };
export default function Login({ onSuccess }: Props) {
  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    onSuccess();
  }
  return (
    <div style={{ display: "grid", placeItems: "center", minHeight: "100vh" }}>
      <form onSubmit={handleSubmit} style={{ width: 320, display: "grid", gap: 12 }}>
        <h1 style={{ fontSize: 24, fontWeight: 700 }}>Connexion</h1>
        <input placeholder="Email" required />
        <input placeholder="Mot de passe" type="password" required />
        <button type="submit">Se connecter</button>
      </form>
    </div>
  );
}

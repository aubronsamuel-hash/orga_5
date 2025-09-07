export default function Avatar({ name }: { name: string }) {
  const initials = name.split(" ").map(p => p[0]?.toUpperCase() || "").slice(0,2).join("");
  const style: React.CSSProperties = {
    width: 32,
    height: 32,
    borderRadius: 999,
    display: "grid",
    placeItems: "center",
    fontSize: 14,
    background: "#e5e7eb",
  };
  return <div style={style}>{initials}</div>;
}

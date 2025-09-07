export function saveAuth(token: string, user: { id: string; email: string }): void {
  localStorage.setItem("auth.token", token);
  localStorage.setItem("auth.user", JSON.stringify(user));
}

export function getToken(): string | null {
  return localStorage.getItem("auth.token");
}

export function isAuthenticated(): boolean {
  return getToken() !== null;
}

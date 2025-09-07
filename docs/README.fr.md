# Guide de démarrage (Windows)

1. Installer [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. Cloner le dépôt et ouvrir PowerShell 7.
3. Copier `.env.example` vers `.env` puis ajuster si besoin.
4. Exécuter `./PS1/dev_up.ps1` pour lancer la pile.
5. Ouvrir http://localhost:8080 et vérifier `/api/healthz`.
6. Lancer `./PS1/smoke.ps1` pour les tests rapides.
7. Pour arrêter: `./PS1/dev_down.ps1`.

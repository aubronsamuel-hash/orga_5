# Frontend

## Installation

Use Node LTS.

Run:

```
npm ci
```

### Lockfile policy
This repository uses npm as the package manager. Always commit `frontend/package-lock.json` to ensure reproducible builds and better CI caching.

In CI:
- If `package-lock.json` exists, the workflow uses `npm ci`.
- If it is missing, CI generates one with `npm install --package-lock-only --no-audit --no-fund` and emits a warning, then proceeds. Please commit the lockfile locally to avoid the warning and to guarantee reproducibility.

On the default branch, a lightweight guard may fail if `frontend/package-lock.json` is missing.

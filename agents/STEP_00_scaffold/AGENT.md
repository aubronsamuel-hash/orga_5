# STEP 00 - Scaffold MVP

## GOAL
Create a minimal working monorepo with CI and Windows-first scripts.

## DELIVERABLES
- backend/: FastAPI with `/healthz`, Alembic init, pytest + coverage config.
- frontend/: Vite + React + TS, Tailwind + shadcn, Storybook, Vitest, Playwright smoke.
- deploy/dev/: `compose.yaml` and `Caddyfile`.
- PS1/: `dev_up.ps1`, `dev_down.ps1`, `seed.ps1`, `smoke.ps1`.
- .github/workflows/: `backend.yml`, `frontend.yml`.
- docs/: `README.fr.md`; root `.env.example`.
- `.github/PULL_REQUEST_TEMPLATE.md`.

## FILES TO CREATE OR MODIFY
List all files explicitly in the PR description. Keep diffs small and readable.

## TEST PLAN (LOCAL)
1) `./PS1/dev_up.ps1`
2) Open http://localhost:8080
3) Check http://localhost:8080/api/healthz returns `{ "status": "ok" }`
4) `./PS1/smoke.ps1` (pytest, vitest, playwright smoke)

## CI GATES
- backend.yml: pytest with coverage >= 80 pct.
- frontend.yml: lint, unit, Playwright smoke (install browsers with `--with-deps`).

## GIT AND PR PLAN
Branch: `feat/step-00-scaffold`
PR title: `feat: scaffold MVP (monorepo, CI, PS1, compose)`
Labels: area/backend, area/frontend, ci, scripts, docs
PR Body sections: Summary, Deliverables, How to run (Windows), Test Plan, Risks, Checklist

## DONE CRITERIA
- Local smoke passes. CI green on the PR. Docs instruct Windows users clearly.

## POST-MERGE UPDATE
- Update root `AGENT.md` CHANGELOG.
- Tick STEP 00 in BACKLOG.
- Set CURRENT TASK to `agents/STEP_01_auth_rbac/AGENT.md`.

## CHANGELOG
- (empty)

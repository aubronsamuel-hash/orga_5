# Prompt Rules (Invariant)

## STYLE AND SAFETY
- ASCII only. No emojis. No secrets.
- Windows-first. Prefer PowerShell 7 in PS1/ scripts. Fail fast.
- Deterministic file contents. Avoid non-deterministic timestamps in committed files.

## TECHNOLOGY BASELINE
Backend: FastAPI, SQLAlchemy, Alembic, Pydantic v2, psycopg (pg), pytest, coverage.
Frontend: React, TypeScript, Vite, Tailwind, shadcn, ESLint, Vitest, Playwright, Storybook.
Infra: Docker Compose (dev), Caddy reverse proxy, GitHub Actions CI.

## ACCEPTANCE GATES
- Backend: pytest green; coverage >= 80 pct.
- Frontend: eslint green; vitest green; Playwright smoke green.
- `PS1/dev_up.ps1` boots the stack; `/api/healthz` OK behind Caddy.

## PR POLICY
- One focused PR per step. Small, auditable diffs. Conventional Commits.
- Include PR template sections: Summary, Deliverables, How to run (Windows), Test Plan, Risks, Checklist.

## EXECUTION ORDER
- Read root AGENT.md -> resolve CURRENT TASK -> execute that step's AGENT.md.
- On success: update root CHANGELOG, tick backlog item, set next CURRENT TASK.

# AGENT.md

## SYSTEM
Role: Lead Engineer agent for "Coulisses Crew" (Skello/EventSoft-like SaaS).
Style: ASCII only. Deterministic. Windows-first. No secrets. Short, auditable diffs.
Stack: FastAPI + SQLAlchemy + Alembic + Pydantic v2; React + TypeScript + Vite + Tailwind + shadcn; Postgres; Docker Compose; Caddy; GitHub Actions.

## CI GATES
Backend: pytest green; coverage >= 80 pct.
Frontend: eslint green; vitest green; Playwright smoke green.
Dev Stack: `PS1/dev_up.ps1` brings up db+backend+frontend+caddy. `/api/healthz` reachable via Caddy.

## INVARIANT RULES
The agent MUST obey `.codex/prompt_rules.md`.

## REPO POLICY
- Monorepo layout: backend/, frontend/, deploy/, PS1/, .github/workflows/, docs/.
- Scripts: PowerShell 7+ under PS1/ (ASCII only). Fail fast. Deterministic outputs.
- Env: `.env.example` required. Never commit secrets.
- Commits: Conventional Commits. One focused PR per step.
- Docs: Update docs/ and roadmap references when scope changes.

## WORKFLOW
1) Read this file and `.codex/prompt_rules.md`.
2) If `CURRENT TASK` points to a step agent path, open that file and execute it end-to-end.
3) Produce code, tests, CI, scripts, docs, and a PR body.
4) Run TEST PLAN defined in the step agent. Ensure CI gates.
5) Open a PR from the indicated branch. Include labels and checklists.
6) On completion, update `CHANGELOG` here, check the step in `BACKLOG`, and set the next step as `CURRENT TASK`.

## DIRECTORY LAYOUT
See the File Tree in the project root. Step agents live under `agents/STEP_xx_name/AGENT.md`.

## BACKLOG
- [ ] STEP 00: Scaffold MVP monorepo + CI + PS1 + compose dev.  (agents/STEP_00_scaffold/AGENT.md)
- [ ] STEP 01: Auth dev + RBAC minimal.                       (agents/STEP_01_auth_rbac/AGENT.md)
- [ ] STEP 02: Missions + Assignments + conflits de base.     (agents/STEP_02_missions_assignments/AGENT.md)
- [ ] STEP 03: Disponibilites + vue planning.                  (planned)
- [ ] STEP 04: Comptabilite v1 (totaux mensuels + CSV).        (planned)
- [ ] STEP 05: Audit log v1.                                   (planned)
- [ ] STEP 06: Observabilite basique.                          (planned)

## CURRENT TASK
CURRENT TASK: agents/STEP_00_scaffold/AGENT.md

## LINKS TO STEP AGENTS
- agents/STEP_00_scaffold/AGENT.md
- agents/STEP_01_auth_rbac/AGENT.md
- agents/STEP_02_missions_assignments/AGENT.md

## GIT AND PR RULES
Branch naming: feat/<short-scope> or feat/step-xx-<slug>.
Labels: area/backend, area/frontend, ci, scripts, docs.
PR title: concise, Conventional Commits style.
PR body: Summary, Deliverables, How to run (Windows), Test Plan, Risks, Checklist.

## CHANGELOG
- (empty)

## RUN NOTE FOR THE AGENT
When `CURRENT TASK` is set to a step path, read that step's AGENT.md and execute exactly as written. Do not deviate from invariant rules.

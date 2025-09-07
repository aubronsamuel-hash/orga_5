# STEP 01 - Auth dev + RBAC minimal

## GOAL
Introduce development auth (fake provider acceptable) and minimal RBAC roles: admin, planner, tech.

## DELIVERABLES
- Backend: `/auth/login` (dev), role model, dependency to enforce roles; tests.
- Frontend: basic auth flow (dev), role-aware UI toggles; tests.
- Docs: brief on roles and dev auth toggle.

## FILES TO CREATE OR MODIFY
- backend: auth routes, role enums, guards, tests.
- frontend: auth context/store, login form (dev), tests.

## TEST PLAN (LOCAL)
- Backend unit tests for role checks.
- Frontend unit tests for role-gated components.

## CI GATES
- All green (backend, frontend, smoke).

## GIT AND PR PLAN
Branch: `feat/step-01-auth-rbac`
PR title: `feat: auth dev and minimal RBAC`

## DONE CRITERIA
- Role enforcement proven by tests. UI reacts to role.

## CHANGELOG
- (empty)

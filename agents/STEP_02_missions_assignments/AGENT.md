# STEP 02 - Missions, Assignments, and Conflict Detection

## GOAL
Introduce Missions and Assignments models and endpoints with basic schedule conflict detection.

## DELIVERABLES
- Backend: models, migrations, endpoints, conflict check; tests.
- Frontend: create mission + assign tech, show conflicts; tests.
- Docs: API and UI notes.

## FILES TO CREATE OR MODIFY
- backend: models, CRUD, routes, tests, Alembic migration.
- frontend: forms, calendar/list view, tests.

## TEST PLAN (LOCAL)
- Unit tests for overlap detection.
- UI tests creating assignments and observing conflict badges.

## CI GATES
- All green (backend, frontend, smoke).

## GIT AND PR PLAN
Branch: `feat/step-02-missions-assignments`
PR title: `feat: missions, assignments, conflict detection`

## DONE CRITERIA
- Conflicts detected deterministically by unit tests.

## CHANGELOG
- (empty)

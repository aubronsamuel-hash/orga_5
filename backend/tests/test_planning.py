from datetime import datetime, timezone

from fastapi.testclient import TestClient
from datetime import datetime, timezone
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from app.main import app
from app.db import Base, get_session
from app.planning import Event

engine = create_engine("sqlite:///./test.db", future=True)
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base.metadata.create_all(engine)


@pytest.fixture(autouse=True)
def clean_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    yield

def override_session():
    with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[get_session] = override_session


def create_event(session, **kwargs):
    evt = Event(**kwargs)
    session.add(evt)
    session.commit()
    return evt


def test_list_events_range():
    with TestingSessionLocal() as session:
        create_event(
            session,
            org_id=1,
            project_id=None,
            title="A",
            start_utc=datetime(2025, 1, 1, tzinfo=timezone.utc),
            end_utc=datetime(2025, 1, 1, 1, tzinfo=timezone.utc),
            location=None,
            notes=None,
            created_at_utc=datetime(2025, 1, 1, tzinfo=timezone.utc),
            updated_at_utc=datetime(2025, 1, 1, tzinfo=timezone.utc),
        )
    client = TestClient(app)
    resp = client.get(
        "/v1/planning/events",
        params={
            "from": "2025-01-01T00:00:00Z",
            "to": "2025-02-01T00:00:00Z",
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 1
    assert data[0]["title"] == "A"


def test_get_event_not_found():
    client = TestClient(app)
    resp = client.get("/v1/planning/events/999")
    assert resp.status_code == 404


def test_get_event():
    with TestingSessionLocal() as session:
        evt = create_event(
            session,
            org_id=1,
            project_id=None,
            title="B",
            start_utc=datetime(2025, 1, 2, tzinfo=timezone.utc),
            end_utc=datetime(2025, 1, 2, 1, tzinfo=timezone.utc),
            location=None,
            notes=None,
            created_at_utc=datetime(2025, 1, 2, tzinfo=timezone.utc),
            updated_at_utc=datetime(2025, 1, 2, tzinfo=timezone.utc),
        )
        event_id = evt.id
    client = TestClient(app)
    resp = client.get(f"/v1/planning/events/{event_id}")
    assert resp.status_code == 200
    assert resp.json()["title"] == "B"

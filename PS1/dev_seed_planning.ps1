param()
python - <<'PY'
from datetime import datetime, timezone
from app.db import Base, engine, SessionLocal
from app.planning import Event
Base.metadata.create_all(engine)
with SessionLocal() as s:
    if not s.query(Event).count():
        e = Event(
            org_id=1,
            project_id=None,
            title="Demo",
            start_utc=datetime(2025,1,1,tzinfo=timezone.utc),
            end_utc=datetime(2025,1,1,1,tzinfo=timezone.utc),
            location=None,
            notes=None,
            created_at_utc=datetime(2025,1,1,tzinfo=timezone.utc),
            updated_at_utc=datetime(2025,1,1,tzinfo=timezone.utc),
        )
        s.add(e)
        s.commit()
PY

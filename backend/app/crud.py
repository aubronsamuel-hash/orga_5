from sqlalchemy.orm import Session
from . import models

def seed_minimal(db: Session):
    if db.query(models.User).count() > 0:
        return
    u1 = models.User(email="camille@orga.test", full_name="Camille Dupont", avatar_url=None)
    u2 = models.User(email="alex@orga.test", full_name="Alex Martin", avatar_url=None)
    db.add_all([u1, u2])
    db.commit()

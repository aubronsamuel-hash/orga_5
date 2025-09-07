import os
from uuid import uuid4

from sqlalchemy import select

from .core.security import hash_password
from .db import SessionLocal
from .models import User


def main() -> None:
    email = os.getenv("SEED_EMAIL", "admin@example.com").lower()
    password = os.getenv("SEED_PASSWORD", "ChangeMe123!")
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.email == email))
        if not user:
            db.add(
                User(id=str(uuid4()), email=email, password_hash=hash_password(password))
            )
            db.commit()


if __name__ == "__main__":
    main()

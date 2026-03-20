from datetime import datetime, timedelta

from app.db import SessionLocal, Base, engine
from app.dependencies.auth import hash_password
from app.models.expense import Expense
from app.models.user import User


def main() -> None:
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == "jeremy").first()
        if not user:
            user = User(
                username="jeremy",
                email="jeremy@example.com",
                hashed_password=hash_password("testpass123"),
            )
            session.add(user)
            session.commit()
            session.refresh(user)

        if session.query(Expense).filter(Expense.user_id == user.id).count() == 0:
            now = datetime.utcnow()
            expenses = [
                Expense(user_id=user.id, amount=2.50, category="coffee", description="Flat white", date=now),
                Expense(user_id=user.id, amount=14.20, category="food", description="Lunch", date=now - timedelta(days=1)),
                Expense(user_id=user.id, amount=45.00, category="shopping", description="Groceries", date=now - timedelta(days=2)),
            ]
            session.add_all(expenses)
            session.commit()
    finally:
        session.close()


if __name__ == "__main__":
    main()

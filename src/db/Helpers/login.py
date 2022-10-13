from sqlalchemy.orm import Session

from src.models.user import User


def get_user(username: str, db: Session):
    user = db.query(User).filter(User.email == username).first()
    return user

from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from src.db.session import get_db
from src.db.Helpers.user import create_new_user
import sys
from src.schemas.user import UserCreate, ShowUser
sys.path.append("")


router = APIRouter()


@router.post("/create", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user

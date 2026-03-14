from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.database import get_db
from app.services import user_service

router = APIRouter(prefix="/users")


@router.get("/")
def get_users(db: Session = Depends(get_db)):

    return user_service.list_users(db)


@router.post("/")
def create_user(email: str, password: str, db: Session = Depends(get_db)):

    return user_service.create_user(db, email, password)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.services import order_service

router = APIRouter(prefix="/orders")


@router.get("/")
def list_orders(db: Session = Depends(get_db)):

    return order_service.get_orders(db)


@router.post("/")
def create_order(user_id: int, product_id: int, db: Session = Depends(get_db)):

    return order_service.create_order(db, user_id, product_id)
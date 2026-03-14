from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.services import product_service
from app.repository import product_repo

router = APIRouter(prefix="/products")


@router.get("/")
def list_products(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):

    offset = (page - 1) * limit

    return db.query(Product).offset(offset).limit(limit).all()


@router.post("/")
def create_product(name: str, price: int, db: Session = Depends(get_db)):

    return product_repo.create_product(db, name, price)
from sqlalchemy.orm import Session
from app.models.order import Order


def create_order(db: Session, user_id, product_id):

    order = Order(user_id=user_id, product_id=product_id)

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


def get_orders(db: Session):

    return db.query(Order).all()
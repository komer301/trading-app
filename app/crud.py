from sqlmodel import select, Session
from fastapi import HTTPException
from app.models import Order, OrderCreate

def create_order(session: Session, order: OrderCreate) -> Order:
    try:
        db_order = Order(**order.model_dump())
        session.add(db_order)
        session.commit()
        session.refresh(db_order)
        return db_order
    except Exception as e:
        session.rollback()  # ✅ Rollback in case of failure
        raise HTTPException(status_code=500, detail=f"Failed to create order: {str(e)}")

def read_orders(session: Session):
    statement = select(Order)
    return session.exec(statement).all()

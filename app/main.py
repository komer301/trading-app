from fastapi import FastAPI, Depends, HTTPException, status
from typing import List, Annotated
from sqlmodel import Session
from app.database import lifespan, get_session
from app.models import Order, OrderCreate
from app.crud import create_order, read_orders

app = FastAPI(lifespan=lifespan)

SessionDep = Annotated[Session, Depends(get_session)]

@app.post("/orders", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order_api(order: OrderCreate, session: SessionDep):
    return create_order(session, order)

@app.get("/orders", response_model=List[Order], status_code=status.HTTP_200_OK)
def read_orders_api(session: SessionDep):
    orders = read_orders(session)
    if not orders:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No orders found")
    return orders

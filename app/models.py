from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum
from pydantic import Field as PydanticField

class OrderType(str, Enum):
    buy = "buy"
    sell = "sell"

class OrderBase(SQLModel):
    symbol: str = PydanticField(..., min_length=1)
    quantity: int = PydanticField(..., gt=0)
    price: float = PydanticField(..., gt=0)
    order_type: OrderType 

class OrderCreate(OrderBase):
    pass

class Order(OrderBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

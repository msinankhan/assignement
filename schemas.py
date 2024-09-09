from pydantic import BaseModel
from typing import List, Optional

class CustomerBase(BaseModel):
    name: str
    email: str
    address: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    customer_id: int
    product_ids: List[int]

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    total_price: float

    class Config:
        orm_mode = True

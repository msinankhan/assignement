from sqlalchemy.orm import Session
from models import Customer, Product, Order
from schemas import CustomerCreate, ProductCreate, OrderCreate

# CRUD for Customers
def create_customer(db: Session, customer: CustomerCreate):
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()

def update_customer(db: Session, customer_id: int, customer: CustomerCreate):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer:
        for key, value in customer.dict().items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer

# CRUD for Products
def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

# CRUD for Orders
def create_order(db: Session, order: OrderCreate):
    db_order = Order(customer_id=order.customer_id)
    total_price = 0
    for product_id in order.product_ids:
        product = get_product(db, product_id)
        if product and product.quantity > 0:
            db_order.products.append(product)
            total_price += product.price
            product.quantity -= 1  
        else:
            raise ValueError("Product not available or out of stock")
    db_order.total_price = total_price
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

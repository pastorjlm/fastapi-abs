
from sqlalchemy import Boolean, Column, Integer, String,ForeignKey,Date
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    email = Column(String(255))
    phone = Column(Integer)
    address=Column(String(255))
    zipCode= Column(Integer)
    city= Column(String(255))
    password= Column(String(255))
    subs =Column(Integer,nullable=True)
    items = relationship("Item", back_populates="owner")




class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, index=True)
    order_id= Column(String(255))
    owner_id = Column(Integer, ForeignKey("users.id"))
    order_date=Column(Date, default=datetime.now(), nullable=True)
    

    owner = relationship("Users", back_populates="items")   
    
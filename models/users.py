from sqlalchemy import Boolean, Column, Integer, String

from config.database import Base


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
    
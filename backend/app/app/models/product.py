from app.db.base_class import Base
from app.models.user import User
from sqlalchemy import String, Integer, ForeignKey, Column, Date
from datetime import datetime


class Product(Base):
    id = Column(Integer, default=0)
    name = Column(String, default='')
    date = Column(Date, default=datetime.now(), nullable=False)
    qty = Column(Integer)
    price = Column(Integer)
    total = Column(Integer)
    category = Column(String)

from app.db.base_class import Base
from sqlalchemy import String, Integer, ForeignKey, Column, Date, relationship
from app.models.user import User
from app.schemas.order.order_add import Status

class Order(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    order_id = Column(Integer, default=1, nullable=False)
    date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")
    products = relationship("Product", back_populates="order", cascade="all, delete, delete-orphan")


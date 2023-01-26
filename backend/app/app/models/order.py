from app.db.base_class import Base
from sqlalchemy import String, Integer, ForeignKey, Column, Date
from app.models.user import User
from app.schemas.order.order_add import Status

class Order(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    order_id Column(Integer, default=1, nullable=False)
    date = Column(Date, nullable=False)
    user = ForeignKey(User, )
    product = Column(Product, on_delete="cascade, on_delete", uselist=True)
    status = Column(String, default=Status.PENDING, nullable=False)


from app.db.base_class import Base
from sqlalchemy import String, Column, ForeignKey, Integer, relationship

class User(Base):
    id = Column(Integer)
    name = Column(Integer)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    creditCard = Column(Integer)
    order = relationship("Order", back_populates="user", collection_class=(set or list))

# user = User(name="", firstname="", lastName="", email="", creditCard=123.4234.23)
# product1 = Prorduct(name="data", date="", qty=2, price=23.4, category="value", total=column_property(qty * price))
# product2 = Prorduct(name="data2", date="", qty=3, price=34.5, category="", total=column_property(qty * price))
# order = Order(user=user, date="")
# order.products.append(product1)
# order.products.append(product2)
# user.order.append(order)
# user.order.add(order)




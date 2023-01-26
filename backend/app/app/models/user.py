from app.db.base_class import Base
from sqlalchemy import String, Column, ForeignKey, Integer,

class User(Base):
    id = Column(Integer)
    name = Column(Integer)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    creditCard = Column(Integer)
    order = Column()


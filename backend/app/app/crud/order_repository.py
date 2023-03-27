from sqlalchemy import Session
from app.models.order import Order
from app.models.user import User
from app.crud.user_repository import UserRepository;

class OrderRepository:
    def __init__(self):
        self.userRepository = UserRepository()

    def saveOrder(db: Session, userId: int, order: Order):
        user = self.userRepository.findUserById(db, userId)
        if user is not None:
            order = user.setOrder(order)
            db.add(order)
            db.commit()
            return order
        return None

    def findOrderById(db: Session, orderId: int):
        order = db.find(Order).filter(Order.getId() == orderId).first()
        return order;

    def deleteOrder(db: Session, orderId: int):
        order = self.findOrderById(orderId)
        if order is not None:
            db.delete(order)
            db.commit()




from sqlalchemy import Session
from app.models.order import Order
from app.models.user import User
from app.crud.user_repository import UserRepository;

class OrderRepository:
    def __init__(self):
        # super(OrderRepository, self).__init__()
        self.db = Session()
        self.userRepository = UserRepository()

    def saveOrder(userId: int, order: Order):
        user = self.userRepository.findUserById(userId)
        if user is not None:
            order = user.setOrder(order)
            self.db.add(order)
            self.db.commit()
            return order
        return None

    def findOrderById(orderId: int):
        order = self.db.find(Order).filter(Order.getId() == orderId).first()
        return order;

    def deleteOrder(orderId: int):
        order = self.findOrderById(orderId)
        if order is not None:
            self.db.delete(order)
            self.commit()




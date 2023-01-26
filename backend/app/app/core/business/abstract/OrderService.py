from app.models.order import Order
from app.db.base import Base


class OrderService:
    def __init__(self, orderRepository):
        self.orderRepository = orderRepository

    def create(self, user_id: User, order: Order):
        order = self.orderRepository.save(user_id, order)
        return order

    def update(self, user_id: User, order: Order):
        order = self.orderRepository.update(user_id, order)
        return order

    def delete(self, order_id: Order):
        self.orderRepository.deleteOrder(order_id)

    def get(self, order_id: Order):
        order = self.orderRepository.findOrderById(order_id)
        return order


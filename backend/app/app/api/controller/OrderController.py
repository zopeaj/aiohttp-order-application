from aiohttp.web import RouteTableDef
from app.core.abstract.business.OrderService import OrderService
from fastapi import jsonable_encoder
from aiohttp.web import Response

orderrouter = RouteTableDef()

class OrderController:
    orderService: OrderService = OrderService()
    userService: UserService = UserService()

    @routerDef.post("/user/order/")
    def addOrderByUser(request):
        user_id = request.get_param("userId")
        user = self.userService.getUserById(user_id)
        order = request.json()
        order_data = jsonable_encoder(order)
        data = self.orderService.create(user_id, order_data)
        if data:
            return Response(body=data, status=201, headers={'Authorization': f'Bearer {user.getToken()}'})
        return Response(body={"detail": "failed"}, status=400)

    @routerDef.put("/user/order/{id}")
    def putOrderByUser(request):
        user_id = request.get_param("userid")
        user = self.userService.getUserById(user_id)
        order = request.json()
        order_data = jsonable_encoder(order)
        if not user:
            return Response(body={"detail": f"user with {user_id} not found"}, status=404)
        order = self.orderService.update(user_id, order_data)
        return Response(body=data, status=203, headers={"Authorization": f"Bearer {user.getToken()}"})

    @routerDef.get("/user/order/{id}")
    def getOrderByUser(request):
        user_id = request.get_param("userid")
        user = self.userService.getUserById(user_id)
        order = user.getOrders()
        if len(order) > 0:
            return Response(body=order, status=200, headers={"Authorization": f"Bearer {user.getToken()}"})
        return Response(body={"detail": "No other found for user"}, status=204, headers={"Authorization": f"Bearer {user.getToken}"})

    @routerDef.delete("/user/order/{id}")
    def removeOrderByUser(request):
        order_id = request.get_param("orderid")
        order = self.orderService.getOrderById(order_id)
        if order is not None:
            self.orderService.delete(order)
            return Response()



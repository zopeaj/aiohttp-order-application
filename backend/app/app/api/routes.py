from backend.app.api.controller.OrderController import orderroutes
from backend.app.api.controller.ProductController import productroutes
from backend.app.api.controller.UserController import userroutes

def setup_routes(app):
    app.add_routes(orderroutes)
    app.add_routes(productroutes)
    app.add_routes(userroutes)


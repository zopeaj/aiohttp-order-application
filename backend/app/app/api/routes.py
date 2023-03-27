import os
import sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.api.controller.OrderController import orderroutes
from app.api.controller.ProductController import productroutes
from app.api.controller.UserController import userroutes

def setup_routes(app):
    app.add_routes(orderroutes)
    app.add_routes(productroutes)
    app.add_routes(userroutes)


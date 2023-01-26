from aiohttp import web
from app.api.routes import setup_routes
from app.api.middleware import error_middleware

app = web.Application()
setup_routes(app)
app.middleware.append(error_middleware)
web.run_app(app, host="127.0.0.1", port=8081)

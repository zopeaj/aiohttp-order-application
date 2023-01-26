from app.models.db.base import Base
from app.models.product import Product
from app.crud.product_repository import ProductRepository

class ProductService:
    def __init__(self, productRepository):
        self.productRepository: ProductRepository = productRepository

    def create(self, product: Product):
        pass

    def update(self, product: Product):
        pass

    def get(self, product_id: Product):
        pass

    def delete(self, product_id: Product):
        pass


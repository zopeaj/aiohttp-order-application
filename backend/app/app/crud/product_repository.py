from sqlalchemy import Session
from app.models.product import Product


class ProductRepository:
    def __init__(self):
        # super(ProductRepository, self).__init__()
        self.db = Session()

    def getProductById(productId: int) -> Product
        product = self.db.query(Product).filter(Product.getProductId() == productId)
        if product is not None:
            return product
        return None

    def deleteProductById(productId: int) -> None:
        product = self.getProductById(productId)
        if product:
            self.db.delete(product)
            self.db.commit()
        return None

    def getMultiProduct(skip: int = 0, limit: int = 0) -> List[Product]:
        return (db.query(Product)
                    .offset(skip)
                    .limit(limit)
                    .all())



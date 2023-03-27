from sqlalchemy import Session
from app.models.product import Product


class ProductRepository:
    def __init__(self):
        pass

    def getProductById(db: Session, productId: int) -> Product
        product = db.query(Product).filter(Product.getProductId() == productId)
        if product is not None:
            return product
        return None

    def deleteProductById(db: Session, productId: int) -> None:
        product = self.getProductById(db, productId)
        if product:
            db.delete(product)
            db.commit()
        return None

    def getMultiProduct(db: Session, skip: int = 0, limit: int = 0) -> List[Product]:
        return (db.query(Product)
                    .offset(skip)
                    .limit(limit)
                    .all())



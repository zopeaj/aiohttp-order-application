from aiohttp.web import RouteTableDef, Response
from app.core.abstract.business.ProductService import ProductService
from fastapi import jsonable_encoder

productrouter = RouteTableDef()

class ProductController:
    productService: ProductService = ProductService()

    @productrouter.get("/products/")
    def getAllAvailableProduct(self, request):
        product = self.productService.getAllAvailableProduct()
        return Response(body=product, status=200)

    @productrouter.post("/products/category")
    def postProduct(self, request):
        data = request.json()
        product_data = jsonable_encoder(data)
        product = self.productService.save(product_data)
        return Response(body=product, status=201)

    @productrouter.put("/products/{id}/category/{name}")
    def updateProduct(self, request, id, name):
        data = request.json()
        productId = request.get_param("productId")
        product = self.productService.getProductById(productId)
        if product is not None:
            product = self.productService.updateProduct(product)
            return Response(body=product, status=201)
        return Response(body={"No data": "error"})

    @productrouter.delete("/products/{id}/category/{category}")
    def deleteProduct(self, request, id, name):
        product_id = request.get_param("productId")
        product = self.productService.getProductById(product_id)
        if product:
            self.productService.deleteProduct(product)
            return Response(body={"details": "product deleted"}, status=204, text="No content")
        return Response(body={"details": "product not found"}, status=404, text="Product not found")





import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from aiohttp.web import RouteTableDef, Response
from app.core.business.abstract.ProductService import ProductService
from fastapi import jsonable_encoder

productrouter = RouteTableDef()

productService: ProductService = ProductService()

@productrouter.get("/products/")
def getAllAvailableProduct(request):
    product = productService.getAllAvailableProduct()
    return Response(body=product, status=200)

@productrouter.post("/products/category")
def postProduct(request):
    data = request.json()
    product_data = jsonable_encoder(data)
    product = productService.save(product_data)
    return Response(body=product, status=201)

@productrouter.put("/products/{productid}/category/{name}")
def updateProduct(request, id, name):
    data = request.json()
    productId = request.match_info.get("productId")
    name = request.match_info.get("name")
    product = productService.getProductById(productId)
    if product is not None:
        product = productService.updateProduct(product)
        return Response(body=product, status=201)
    return Response(body={"No data": "error"})

@productrouter.delete("/products/{productid}/category/{category}")
def deleteProduct(request, id, name):
    product_id = request.match_info.get("productId")
    category = request.match_info.get("category")
    product = productService.getProductById(product_id)
    if product:
        productService.deleteProduct(product)
        return Response(body={"details": "product deleted"}, status=204, text="No content")
    return Response(body={"details": "product not found"}, status=404, text="Product not found")





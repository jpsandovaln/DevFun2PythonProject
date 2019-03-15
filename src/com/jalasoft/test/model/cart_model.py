from src.com.jalasoft.test.db.product_query import ProductQuery


class CartModel:
    def __init__(self):
        print("cartModel class")

    def saveProduct(self, product):
        print(product)
        query = ProductQuery()
        query.insertProduct(product)

    def getAllProduct(self):
        query = ProductQuery()
        return query.loadAllProduct()


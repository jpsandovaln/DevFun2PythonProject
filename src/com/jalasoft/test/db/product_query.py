from src.com.jalasoft.test.db.connection_db import ConnectionDB
from src.com.jalasoft.test.model.product import Product


class ProductQuery:
    def __init__(self):
        self.__conn = ConnectionDB().getConnection()

    def insertProduct(self, product):
        cursor = self.__conn.cursor()
        insertQuery = "insert into product(name, price) values ('" + product.getProductName() + "', " + str(product.getPrice())+ ");"
        print(insertQuery)
        cursor.execute(insertQuery)
        self.__conn.commit()

    def loadAllProduct(self):
        cursor = self.__conn.cursor()
        cursor.execute("select name, price from product;")
        rows = cursor.fetchall()
        productList = []
        for row in rows:
            prod = Product()
            prod.setProductName(row[0])
            prod.setProductName(row[1])
            productList.append(prod)

        return productList



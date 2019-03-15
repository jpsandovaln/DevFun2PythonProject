from PyQt5.QtWidgets import QTableWidgetItem
from src.com.jalasoft.test.view.product_insert_view import ProductInsertView
from src.com.jalasoft.test.model.product import Product


class CartController:

    def __init__(self, mainView, cartModel):
        self.mainView = mainView
        self.cartModel = cartModel
        self.mainView.initUI(self)

    def addActionListener(self):
        self.centralWidget = self.mainView.centralWidget()
        if isinstance(self.centralWidget, ProductInsertView):
            self.centralWidget.getSaveProductButton().clicked.connect(lambda: self.saveProduct())

    def saveProduct(self):
        pro = Product()
        pro.setProductName(self.centralWidget.getName())
        pro.setPrice(self.centralWidget.getPrice())
        self.cartModel.saveProduct(pro)

    def loadProduct(self):
        self.centralWidget = self.mainView.centralWidget()
        listProduct = self.cartModel.getAllProduct()
        listSize = len(listProduct)
        self.centralWidget.getTable().setRowCount(listSize)
        index = 0
        for prod in listProduct:
            print(prod.getProductName())
            self.centralWidget.getTable().setItem(index, 0, QTableWidgetItem(str(prod.getId())))
            self.centralWidget.getTable().setItem(index, 1, QTableWidgetItem(prod.getProductName()))
            self.centralWidget.getTable().setItem(index, 2, QTableWidgetItem(str(prod.getPrice())))
            index = index + 1


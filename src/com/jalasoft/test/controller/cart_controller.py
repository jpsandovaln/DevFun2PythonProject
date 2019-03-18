from PyQt5.QtWidgets import QTableWidgetItem, QLineEdit
from src.com.jalasoft.test.view.product_insert_view import ProductInsertView
from src.com.jalasoft.test.view.product_show_view import ProductShowView
from src.com.jalasoft.test.model.product import Product


class CartController:

    def __init__(self, mainView, cartModel):
        self.mainView = mainView
        self.cartModel = cartModel
        self.mainView.initUI(self)
        self.cartList = []

    def addActionListener(self):
        self.centralWidget = self.mainView.centralWidget()
        if isinstance(self.centralWidget, ProductInsertView):
            self.centralWidget.getSaveProductButton().clicked.connect(lambda: self.saveProduct())
        if isinstance(self.centralWidget, ProductShowView):
            self.centralWidget.getAddTocartButton().clicked.connect(lambda: self.addToCart())


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
            self.centralWidget.getTable().setItem(index, 0, QTableWidgetItem(str(prod.getId())))
            self.centralWidget.getTable().setItem(index, 1, QTableWidgetItem(prod.getProductName()))
            self.centralWidget.getTable().setItem(index, 2, QTableWidgetItem(str(prod.getPrice())))
            index = index + 1

    def addToCart(self):
        indexes = self.centralWidget.getTable().selectionModel().selectedIndexes()
        id = indexes[0].sibling(indexes[0].row(),indexes[0].column()).data();
        name = indexes[1].sibling(indexes[1].row(), indexes[1].column()).data();
        price = indexes[2].sibling(indexes[2].row(), indexes[2].column()).data();
        #create product and add to cart
        pro = Product()
        pro.setId(id)
        pro.setProductName(name)
        pro.setPrice(price)
        self.cartList.append(pro)
        self.loadCartTable()

    def loadCartTable(self):
        listSize = len(self.cartList)
        self.centralWidget.getCartTable().setRowCount(listSize)
        index = 0
        for prod in self.cartList:
            quantity = QLineEdit()
            self.centralWidget.getCartTable().setItem(index, 0, QTableWidgetItem(str(prod.getId())))
            self.centralWidget.getCartTable().setItem(index, 1, QTableWidgetItem(prod.getProductName()))
            self.centralWidget.getCartTable().setItem(index, 2, QTableWidgetItem(str(prod.getPrice())))
            self.centralWidget.getCartTable().setCellWidget(index, 3, quantity)
            index = index + 1








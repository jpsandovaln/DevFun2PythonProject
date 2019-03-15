from PyQt5.QtWidgets import QApplication
from src.com.jalasoft.test.view.main_view import MainView
from src.com.jalasoft.test.model.cart_model import CartModel


class CartController:

    def __init__(self, mainView, cartModel):
        mainView.initUI()


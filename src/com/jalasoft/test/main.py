import sys
from PyQt5.QtWidgets import QApplication
from src.com.jalasoft.test.controller.cart_controller import CartController
from src.com.jalasoft.test.view.main_view import MainView
from src.com.jalasoft.test.model.cart_model import CartModel


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MainView()
    model = CartModel()
    controller = CartController(view, model)
    sys.exit(app.exec_())

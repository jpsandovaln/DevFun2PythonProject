from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton, QComboBox, QTableWidget, QTableWidgetItem


class ProductShowView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initComponent()

    def initComponent(self):
        vLayout = QVBoxLayout()

        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Product Name", "Price"])

        self.addButton = QPushButton("Add to Cart", self)

        vLayout.addWidget(self.table)
        vLayout.addWidget(self.addButton)

        self.setLayout(vLayout)

    def getTable(self):
        return self.table


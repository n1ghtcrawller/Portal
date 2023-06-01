from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6.QtGui import QIcon
from main_window import Ui_MainWindow
import sys
from start_app import InputValues
from MainTableLogic import MainTable
from registration_logic import RegisterTable

class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('airplane_icon-120x120.png'))
        self.ui.download.clicked.connect(self.OpenInputValues)
        self.ui.analyse.clicked.connect(self.OpenMainTable)
        self.ui.register_data.clicked.connect(self.OpenRegisterTable)
    def OpenMainTable(self):
        self.app = MainTable()
        self.app.show()

    def OpenInputValues(self):
        self.app = InputValues()
        self.app.show()

    def OpenRegisterTable(self):
        self.app = RegisterTable()
        self.app.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    input_values = QtWidgets.QMainWindow()
    application = MainMenu()
    application.show()
    sys.exit(app.exec())

from dialog_register_logic import Registrate
from registration import return_not_registered_values
import json
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QApplication
from PyQt6.QtGui import QIcon
from register_web import Ui_MainWindow



def read(filename):
    with open(filename, 'r', encoding="UTF-8") as file:
        return json.load(file)


data = read("not_registered.json")
length_of_list = len(data["items"])


def adjust_table(col_names, rows, table):
    table.setRowCount(rows)
    table.setColumnCount(len(col_names))
    table.setHorizontalHeaderLabels(col_names)

    for row in range(rows):
        for column in range(len(col_names)):
            table.setItem(row, column, QTableWidgetItem(return_not_registered_values(row, col_names[column])))


class RegisterTable(QtWidgets.QMainWindow):
    def __init__(self):
        super(RegisterTable, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        col_names = ["cirID", "evaluate", "resolve", "is_registered"]
        adjust_table(col_names, length_of_list, self.ui.tableWidget)

    def initUI(self):
        self.setWindowIcon(QIcon('airplane_icon-120x120.png'))
        self.ui.pushButton.clicked.connect(self.OpenRegistrationDialog)
        self.ui.pushButton_2.clicked.connect(self.close)

    def OpenRegistrationDialog(self):
        self.app = Registrate()
        self.app.show()

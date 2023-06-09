from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QApplication
from PyQt6.QtGui import QIcon
from MainTable import Ui_MainWindow
from start_app import InputValues
from SplitTable import return_values
import json


def read(filename):
    with open(filename, 'r', encoding="UTF-8") as file:
        return json.load(file)


data = read("new.json")
length_of_list = len(data["items"])


def adjust_table(col_names, rows, table):
    table.setRowCount(rows)
    table.setColumnCount(len(col_names))
    table.setHorizontalHeaderLabels(col_names)

    for row in range(rows):
        for column in range(len(col_names)):
            table.setItem(row, column, QTableWidgetItem(return_values(row, col_names[column])))


class MainTable(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainTable, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        col_names = ["cirID", "evaluate", "resolve", "is_registered"]
        adjust_table(col_names, length_of_list, self.ui.tableWidget)

    def init_UI(self):
        self.setWindowIcon(QIcon('airplane_icon-120x120.png'))
        self.ui.pushButton.clicked.connect(self.OpenInputValues)
        self.ui.pushButton_3.clicked.connect(self.close)



    def OpenInputValues(self):
        self.app = InputValues()
        self.app.show()


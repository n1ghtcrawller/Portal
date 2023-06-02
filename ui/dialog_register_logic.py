from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog
from dialog_register import Ui_Dialog
import registration


class Registrate(QtWidgets.QDialog):
    def __init__(self):
        super(Registrate, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.pushButton.clicked.connect(self.find_cirID)
        self.ui.buttonBox.accepted.connect(self.register_data)


    def register_data(self):
        input_ID = self.ui.cirID.text()
        registration.transport(input_ID)

    def find_cirID(self):
        input_cirID = self.ui.cirID.text()
        output_answer = registration.finder(input_cirID)
        self.ui.label.setText(str(output_answer))
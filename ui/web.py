# Form implementation generated from reading ui file 'web.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_input_values(object):
    def setupUi(self, input_values):
        input_values.setObjectName("input_values")
        input_values.setFixedSize(532, 609)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        input_values.setFont(font)
        input_values.setStyleSheet("background-color: #00BFFF;")
        input_values.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(parent=input_values)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 381, 131))
        font = QtGui.QFont()
        font.setFamily("Apple Symbols")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("text-align: center;\n"
"color: white;\n"
"border-color: white;\n"
"border-width: 2px;\n"
"font: 75 20pt \"Apple Symbols\";")
        self.label.setObjectName("label")
        self.cirID = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.cirID.setGeometry(QtCore.QRect(70, 160, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Apple Symbols")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cirID.setFont(font)
        self.cirID.setStyleSheet("background-color: #00BFFF;\n"
"color: white;\n"
"font: 30pt \"Apple Symbols\";\n"
"border: 2px solid white;\n"
"border-radius: 30;")
        self.cirID.setFrame(False)
        self.cirID.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cirID.setObjectName("cirID")
        self.applic_vlalue = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.applic_vlalue.setGeometry(QtCore.QRect(70, 230, 380, 61))
        font = QtGui.QFont()
        font.setFamily("Apple Symbols")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.applic_vlalue.setFont(font)
        self.applic_vlalue.setStyleSheet("background-color: #00BFFF;\n"
"color: white;\n"
"font: 30pt \"Apple Symbols\";\n"
"border: 2px solid white;\n"
"border-radius: 30;")
        self.applic_vlalue.setFrame(False)
        self.applic_vlalue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.applic_vlalue.setObjectName("applic_vlalue")
        self.result = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.result.setGeometry(QtCore.QRect(70, 370, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Apple Symbols")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.result.setFont(font)
        self.result.setStyleSheet("background-color: #00BFFF;\n"
"color: white;\n"
"font: 30pt \"Apple Symbols\";\n"
"border: 2px solid white;\n"
"border-radius: 30;")
        self.result.setFrame(False)
        self.result.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result.setObjectName("result")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 300, 381, 61))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: #00BFFF;\n"
"    background-color: white;\n"
"    border: 2px solid rgb(59, 131, 189);\n"
"    border-radius: 30;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(200, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.descript = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.descript.setGeometry(QtCore.QRect(70, 440, 381, 71))
        self.descript.setStyleSheet("    color: #00BFFF;\n"
"    background-color: white;\n"
"    border: 2px solid rgb(59, 131, 189);")
        self.descript.setObjectName("descript")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 520, 301, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: #00BFFF;\n"
"    background-color: white;\n"
"    border: 2px solid rgb(59, 131, 189);\n"
"    border-radius: 30;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(200, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        input_values.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=input_values)
        self.statusbar.setObjectName("statusbar")
        input_values.setStatusBar(self.statusbar)

        self.retranslateUi(input_values)
        QtCore.QMetaObject.connectSlotsByName(input_values)

    def retranslateUi(self, input_values):
        _translate = QtCore.QCoreApplication.translate
        input_values.setWindowTitle(_translate("input_values", "MainWindow"))
        self.label.setText(_translate("input_values", "<html><head/><body><p align=\"center\">Ввод данных для расчёта</p><p align=\"center\">строчных применимостей</p></body></html>"))
        self.pushButton.setText(_translate("input_values", "КОНВЕРТИРОВАТЬ "))
        self.pushButton_2.setText(_translate("input_values", "ПОИСК ДИАПАЗОНОВ"))


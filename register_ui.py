# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 544)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(46, 52, 54);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formWidget = QtWidgets.QWidget(self.centralwidget)
        self.formWidget.setMaximumSize(QtCore.QSize(300, 400))
        self.formWidget.setStyleSheet("QWidget#formWidget {\n"
"    background-color: rgb(130, 130, 130);\n"
"    border: 1px solid rgb(37, 39, 48);\n"
"    border-radius: 12px;\n"
"}")
        self.formWidget.setObjectName("formWidget")
        self.registerLabel = QtWidgets.QLabel(self.formWidget)
        self.registerLabel.setGeometry(QtCore.QRect(80, 20, 140, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.registerLabel.setFont(font)
        self.registerLabel.setStyleSheet("QLabel {\n"
"    background-color: rgb(130, 130, 130);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.registerLabel.setObjectName("registerLabel")
        self.label = QtWidgets.QLabel(self.formWidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 280, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    background-color: rgb(130, 130, 130);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.formWidget)
        self.line.setGeometry(QtCore.QRect(0, 110, 300, 20))
        self.line.setStyleSheet("QFrame#line {\n"
"    color: rgb(130, 130, 130);\n"
"    background-color: rgb(130, 130, 130);\n"
"    margin-left: 20px;\n"
"    margin-right: 20px;\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.usernameInput = QtWidgets.QLineEdit(self.formWidget)
        self.usernameInput.setGeometry(QtCore.QRect(30, 150, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.usernameInput.setFont(font)
        self.usernameInput.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(60, 62, 71);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.usernameInput.setText("")
        self.usernameInput.setObjectName("usernameInput")
        self.passwordInput = QtWidgets.QLineEdit(self.formWidget)
        self.passwordInput.setGeometry(QtCore.QRect(30, 190, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passwordInput.setFont(font)
        self.passwordInput.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(60, 62, 71);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.passwordInput.setText("")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.confirmInput = QtWidgets.QLineEdit(self.formWidget)
        self.confirmInput.setGeometry(QtCore.QRect(30, 230, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.confirmInput.setFont(font)
        self.confirmInput.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(60, 62, 71);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.confirmInput.setText("")
        self.confirmInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmInput.setObjectName("confirmInput")
        self.emailInput = QtWidgets.QLineEdit(self.formWidget)
        self.emailInput.setGeometry(QtCore.QRect(30, 270, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.emailInput.setFont(font)
        self.emailInput.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(60, 62, 71);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.emailInput.setText("")
        self.emailInput.setObjectName("emailInput")
        self.registerButton = QtWidgets.QPushButton(self.formWidget)
        self.registerButton.setGeometry(QtCore.QRect(30, 310, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(5, 110, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(60, 62, 71);\n"
"    background-color: rgb(20, 135, 0);\n"
"}")
        self.registerButton.setObjectName("registerButton")
        self.horizontalLayout.addWidget(self.formWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt Music Archive"))
        self.registerLabel.setText(_translate("MainWindow", "Register"))
        self.label.setText(_translate("MainWindow", "Please fill in this form to create an account."))
        self.usernameInput.setPlaceholderText(_translate("MainWindow", "Username"))
        self.passwordInput.setPlaceholderText(_translate("MainWindow", "Password"))
        self.confirmInput.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.emailInput.setPlaceholderText(_translate("MainWindow", "Email"))
        self.registerButton.setText(_translate("MainWindow", "Register"))

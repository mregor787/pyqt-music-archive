# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget#centralwidget {\n"
"    background-color: rgb(46, 52, 54);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menuWidget = QtWidgets.QWidget(self.centralwidget)
        self.menuWidget.setMaximumSize(QtCore.QSize(930, 690))
        self.menuWidget.setStyleSheet("QWidget#menuWidget {\n"
"    background-color: rgb(130, 130, 130);\n"
"    border: 1px solid rgb(37, 39, 48);\n"
"    border-radius: 12px;\n"
"}")
        self.menuWidget.setObjectName("menuWidget")
        self.label = QtWidgets.QLabel(self.menuWidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 370, 120))
        self.label.setStyleSheet("QLabel {\n"
"    background-color: rgb(130, 130, 130);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.label.setObjectName("label")
        self.profileWidget = QtWidgets.QWidget(self.menuWidget)
        self.profileWidget.setGeometry(QtCore.QRect(70, 180, 230, 180))
        self.profileWidget.setStyleSheet("#menuWidget > QWidget {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"#menuWidget > QWidget:hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.profileWidget.setObjectName("profileWidget")
        self.profileTitle = QtWidgets.QLabel(self.profileWidget)
        self.profileTitle.setGeometry(QtCore.QRect(60, 10, 110, 40))
        self.profileTitle.setStyleSheet("QLabel {\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.profileTitle.setObjectName("profileTitle")
        self.profilePic = QtWidgets.QLabel(self.profileWidget)
        self.profilePic.setGeometry(QtCore.QRect(10, 70, 70, 70))
        self.profilePic.setStyleSheet("")
        self.profilePic.setText("")
        self.profilePic.setPixmap(QtGui.QPixmap("images/profile.png"))
        self.profilePic.setScaledContents(True)
        self.profilePic.setObjectName("profilePic")
        self.profileDescription = QtWidgets.QLabel(self.profileWidget)
        self.profileDescription.setGeometry(QtCore.QRect(85, 60, 140, 90))
        self.profileDescription.setStyleSheet("")
        self.profileDescription.setWordWrap(True)
        self.profileDescription.setObjectName("profileDescription")
        self.searchWidget = QtWidgets.QWidget(self.menuWidget)
        self.searchWidget.setGeometry(QtCore.QRect(350, 180, 230, 180))
        self.searchWidget.setStyleSheet("#menuWidget > QWidget {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"#menuWidget > QWidget:hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.searchWidget.setObjectName("searchWidget")
        self.searchTitle = QtWidgets.QLabel(self.searchWidget)
        self.searchTitle.setGeometry(QtCore.QRect(60, 10, 110, 40))
        self.searchTitle.setStyleSheet("QLabel {\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.searchTitle.setObjectName("searchTitle")
        self.searchPic = QtWidgets.QLabel(self.searchWidget)
        self.searchPic.setGeometry(QtCore.QRect(10, 70, 70, 70))
        self.searchPic.setStyleSheet("")
        self.searchPic.setText("")
        self.searchPic.setPixmap(QtGui.QPixmap("images/search.png"))
        self.searchPic.setScaledContents(True)
        self.searchPic.setObjectName("searchPic")
        self.searchDescription = QtWidgets.QLabel(self.searchWidget)
        self.searchDescription.setGeometry(QtCore.QRect(85, 60, 140, 90))
        self.searchDescription.setStyleSheet("")
        self.searchDescription.setWordWrap(True)
        self.searchDescription.setObjectName("searchDescription")
        self.widget_3 = QtWidgets.QWidget(self.menuWidget)
        self.widget_3.setGeometry(QtCore.QRect(630, 180, 230, 180))
        self.widget_3.setStyleSheet("#menuWidget > QWidget {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"#menuWidget > QWidget:hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.menuWidget)
        self.widget_4.setGeometry(QtCore.QRect(70, 410, 230, 180))
        self.widget_4.setStyleSheet("#menuWidget > QWidget {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"#menuWidget > QWidget:hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.widget_5 = QtWidgets.QWidget(self.menuWidget)
        self.widget_5.setGeometry(QtCore.QRect(350, 410, 230, 180))
        self.widget_5.setStyleSheet("#menuWidget > QWidget {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"#menuWidget > QWidget:hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.widget_5.setObjectName("widget_5")
        self.widget_6 = QtWidgets.QWidget(self.menuWidget)
        self.widget_6.setGeometry(QtCore.QRect(630, 410, 230, 180))
        self.widget_6.setStyleSheet("#menuWidget > QWidget {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"#menuWidget > QWidget:hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout.addWidget(self.menuWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt Music Archive"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">Main Menu</span></p></body></html>"))
        self.profileTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Profile</span></p></body></html>"))
        self.profileDescription.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Editing your profile &amp; account info. Privacy settings.</span></p></body></html>"))
        self.searchTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Search</span></p></body></html>"))
        self.searchDescription.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Search for content in the database, such as tracks, artists, albums, etc.</span></p></body></html>"))
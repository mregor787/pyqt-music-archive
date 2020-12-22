# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
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
        icon.addPixmap(QtGui.QPixmap("images/user_interface/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget#centralwidget {\n"
"    background-color: rgb(46, 52, 54);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.menuPage = QtWidgets.QWidget()
        self.menuPage.setStyleSheet("QWidget#menuPage {\n"
"    background-color: rgb(46, 52, 54);\n"
"}")
        self.menuPage.setObjectName("menuPage")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.menuPage)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menuWidget = QtWidgets.QWidget(self.menuPage)
        self.menuWidget.setMaximumSize(QtCore.QSize(930, 690))
        self.menuWidget.setStyleSheet("QWidget#menuWidget {\n"
"    background-color: rgb(130, 130, 130);\n"
"    border: 1px solid rgb(37, 39, 48);\n"
"    border-radius: 12px;\n"
"}")
        self.menuWidget.setObjectName("menuWidget")
        self.menuTitle = QtWidgets.QLabel(self.menuWidget)
        self.menuTitle.setGeometry(QtCore.QRect(280, 20, 370, 120))
        self.menuTitle.setStyleSheet("QLabel {\n"
"    background-color: rgb(130, 130, 130);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.menuTitle.setObjectName("menuTitle")
        self.toProfileButton = QWidgetClickable(self.menuWidget)
        self.toProfileButton.setGeometry(QtCore.QRect(70, 180, 230, 180))
        self.toProfileButton.setStyleSheet("#menuWidget > #toProfileButton {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"#menuWidget > #toProfileButton:hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.toProfileButton.setObjectName("toProfileButton")
        self.profileButtonTitle = QtWidgets.QLabel(self.toProfileButton)
        self.profileButtonTitle.setGeometry(QtCore.QRect(60, 10, 110, 40))
        self.profileButtonTitle.setStyleSheet("QLabel {\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.profileButtonTitle.setObjectName("profileButtonTitle")
        self.profileButtonPic = QtWidgets.QLabel(self.toProfileButton)
        self.profileButtonPic.setGeometry(QtCore.QRect(10, 70, 70, 70))
        self.profileButtonPic.setStyleSheet("")
        self.profileButtonPic.setText("")
        self.profileButtonPic.setPixmap(QtGui.QPixmap("images/user_interface/profile.png"))
        self.profileButtonPic.setScaledContents(True)
        self.profileButtonPic.setObjectName("profileButtonPic")
        self.profileButtonDescription = QtWidgets.QLabel(self.toProfileButton)
        self.profileButtonDescription.setGeometry(QtCore.QRect(85, 60, 140, 90))
        self.profileButtonDescription.setStyleSheet("")
        self.profileButtonDescription.setWordWrap(True)
        self.profileButtonDescription.setObjectName("profileButtonDescription")
        self.toSearchButton = QWidgetClickable(self.menuWidget)
        self.toSearchButton.setGeometry(QtCore.QRect(350, 180, 230, 180))
        self.toSearchButton.setStyleSheet("#menuWidget > #toSearchButton {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"#menuWidget > #toSearchButton:hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.toSearchButton.setObjectName("toSearchButton")
        self.searchButtonTitle = QtWidgets.QLabel(self.toSearchButton)
        self.searchButtonTitle.setGeometry(QtCore.QRect(60, 10, 110, 40))
        self.searchButtonTitle.setStyleSheet("QLabel {\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.searchButtonTitle.setObjectName("searchButtonTitle")
        self.searchButtonPic = QtWidgets.QLabel(self.toSearchButton)
        self.searchButtonPic.setGeometry(QtCore.QRect(10, 70, 70, 70))
        self.searchButtonPic.setStyleSheet("")
        self.searchButtonPic.setText("")
        self.searchButtonPic.setPixmap(QtGui.QPixmap("images/user_interface/search.png"))
        self.searchButtonPic.setScaledContents(True)
        self.searchButtonPic.setObjectName("searchButtonPic")
        self.searchButtonDescription = QtWidgets.QLabel(self.toSearchButton)
        self.searchButtonDescription.setGeometry(QtCore.QRect(85, 60, 140, 90))
        self.searchButtonDescription.setStyleSheet("")
        self.searchButtonDescription.setWordWrap(True)
        self.searchButtonDescription.setObjectName("searchButtonDescription")
        self.widget_3 = QWidgetClickable(self.menuWidget)
        self.widget_3.setGeometry(QtCore.QRect(630, 180, 230, 180))
        self.widget_3.setStyleSheet("#menuWidget > #widget_3 {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"#menuWidget > #widget_3:hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QWidgetClickable(self.menuWidget)
        self.widget_4.setGeometry(QtCore.QRect(70, 410, 230, 180))
        self.widget_4.setStyleSheet("#menuWidget > #widget_4 {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"#menuWidget > #widget_4:hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.widget_5 = QWidgetClickable(self.menuWidget)
        self.widget_5.setGeometry(QtCore.QRect(350, 410, 230, 180))
        self.widget_5.setStyleSheet("#menuWidget > #widget_5 {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"#menuWidget > #widget_5:hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.widget_5.setObjectName("widget_5")
        self.widget_6 = QWidgetClickable(self.menuWidget)
        self.widget_6.setGeometry(QtCore.QRect(630, 410, 230, 180))
        self.widget_6.setStyleSheet("#menuWidget > #widget_6 {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"#menuWidget > #widget_6:hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2.addWidget(self.menuWidget)
        self.stackedWidget.addWidget(self.menuPage)
        self.profilePage = QtWidgets.QWidget()
        self.profilePage.setStyleSheet("QWidget#profilePage {\n"
"    background-color: rgb(46, 52, 54);\n"
"}")
        self.profilePage.setObjectName("profilePage")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.profilePage)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.profileWidget = QtWidgets.QWidget(self.profilePage)
        self.profileWidget.setMaximumSize(QtCore.QSize(930, 690))
        self.profileWidget.setStyleSheet("QWidget#profileWidget {\n"
"    background-color: rgb(130, 130, 130);\n"
"    border: 1px solid rgb(37, 39, 48);\n"
"    border-radius: 12px;\n"
"}")
        self.profileWidget.setObjectName("profileWidget")
        self.profileMainTitle = QtWidgets.QLabel(self.profileWidget)
        self.profileMainTitle.setGeometry(QtCore.QRect(5, 10, 920, 90))
        self.profileMainTitle.setStyleSheet("QLabel {\n"
"    background-color: rgb(130, 130, 130);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.profileMainTitle.setObjectName("profileMainTitle")
        self.profileTitle_1 = QtWidgets.QLabel(self.profileWidget)
        self.profileTitle_1.setGeometry(QtCore.QRect(60, 90, 380, 40))
        self.profileTitle_1.setObjectName("profileTitle_1")
        self.profileIconWidget = QtWidgets.QWidget(self.profileWidget)
        self.profileIconWidget.setGeometry(QtCore.QRect(50, 150, 310, 220))
        self.profileIconWidget.setStyleSheet("#profileIconWidget {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"}")
        self.profileIconWidget.setObjectName("profileIconWidget")
        self.changeIconButton = QWidgetClickable(self.profileIconWidget)
        self.changeIconButton.setGeometry(QtCore.QRect(220, 110, 40, 40))
        self.changeIconButton.setStyleSheet("#changeIconButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(30, 109, 207);\n"
"}\n"
"#changeIconButton:hover {\n"
"    border: 2px solid rgb(60, 62, 71);\n"
"    background-color: rgb(70, 149, 230);\n"
"}")
        self.changeIconButton.setObjectName("changeIconButton")
        self.changeIconPic = QtWidgets.QLabel(self.changeIconButton)
        self.changeIconPic.setGeometry(QtCore.QRect(5, 5, 30, 30))
        self.changeIconPic.setText("")
        self.changeIconPic.setPixmap(QtGui.QPixmap("images/user_interface/input.png"))
        self.changeIconPic.setScaledContents(True)
        self.changeIconPic.setObjectName("changeIconPic")
        self.profileIconPic = QtWidgets.QLabel(self.profileIconWidget)
        self.profileIconPic.setGeometry(QtCore.QRect(35, 70, 120, 120))
        self.profileIconPic.setStyleSheet("")
        self.profileIconPic.setText("")
        self.profileIconPic.setPixmap(QtGui.QPixmap("images/user_interface/profile.png"))
        self.profileIconPic.setScaledContents(True)
        self.profileIconPic.setObjectName("profileIconPic")
        self.profileIconLabel_1 = QtWidgets.QLabel(self.profileIconWidget)
        self.profileIconLabel_1.setGeometry(QtCore.QRect(20, 30, 150, 30))
        self.profileIconLabel_1.setObjectName("profileIconLabel_1")
        self.profileIconLabel_2 = QtWidgets.QLabel(self.profileIconWidget)
        self.profileIconLabel_2.setGeometry(QtCore.QRect(190, 70, 100, 30))
        self.profileIconLabel_2.setObjectName("profileIconLabel_2")
        self.profileInfoWidget = QtWidgets.QWidget(self.profileWidget)
        self.profileInfoWidget.setGeometry(QtCore.QRect(410, 150, 470, 290))
        self.profileInfoWidget.setStyleSheet("#profileInfoWidget {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"}")
        self.profileInfoWidget.setObjectName("profileInfoWidget")
        self.profileInfoLabel_1 = QtWidgets.QLabel(self.profileInfoWidget)
        self.profileInfoLabel_1.setGeometry(QtCore.QRect(20, 15, 100, 32))
        self.profileInfoLabel_1.setObjectName("profileInfoLabel_1")
        self.profileInfoLabel_2 = QtWidgets.QLabel(self.profileInfoWidget)
        self.profileInfoLabel_2.setGeometry(QtCore.QRect(20, 55, 100, 32))
        self.profileInfoLabel_2.setObjectName("profileInfoLabel_2")
        self.profileFirstNameInput = QtWidgets.QLineEdit(self.profileInfoWidget)
        self.profileFirstNameInput.setGeometry(QtCore.QRect(140, 18, 290, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.profileFirstNameInput.setFont(font)
        self.profileFirstNameInput.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.profileFirstNameInput.setObjectName("profileFirstNameInput")
        self.profileLastNameInput = QtWidgets.QLineEdit(self.profileInfoWidget)
        self.profileLastNameInput.setGeometry(QtCore.QRect(140, 58, 290, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.profileLastNameInput.setFont(font)
        self.profileLastNameInput.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.profileLastNameInput.setObjectName("profileLastNameInput")
        self.profileInfoLabel_3 = QtWidgets.QLabel(self.profileInfoWidget)
        self.profileInfoLabel_3.setGeometry(QtCore.QRect(20, 135, 100, 32))
        self.profileInfoLabel_3.setObjectName("profileInfoLabel_3")
        self.profileBirthdateInput = QtWidgets.QLineEdit(self.profileInfoWidget)
        self.profileBirthdateInput.setGeometry(QtCore.QRect(140, 98, 290, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.profileBirthdateInput.setFont(font)
        self.profileBirthdateInput.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.profileBirthdateInput.setObjectName("profileBirthdateInput")
        self.profileInfoLabel_4 = QtWidgets.QLabel(self.profileInfoWidget)
        self.profileInfoLabel_4.setGeometry(QtCore.QRect(20, 175, 100, 32))
        self.profileInfoLabel_4.setObjectName("profileInfoLabel_4")
        self.profileEmailInput = QtWidgets.QLineEdit(self.profileInfoWidget)
        self.profileEmailInput.setGeometry(QtCore.QRect(140, 178, 290, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.profileEmailInput.setFont(font)
        self.profileEmailInput.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.profileEmailInput.setObjectName("profileEmailInput")
        self.profileInfoLabel_5 = QtWidgets.QLabel(self.profileInfoWidget)
        self.profileInfoLabel_5.setGeometry(QtCore.QRect(20, 95, 100, 32))
        self.profileInfoLabel_5.setObjectName("profileInfoLabel_5")
        self.profileCountryInput = QtWidgets.QLineEdit(self.profileInfoWidget)
        self.profileCountryInput.setGeometry(QtCore.QRect(140, 138, 290, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.profileCountryInput.setFont(font)
        self.profileCountryInput.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(30, 32, 41);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(105, 105, 105);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(115, 115, 115);\n"
"}")
        self.profileCountryInput.setObjectName("profileCountryInput")
        self.profileInfoSaveButton = QtWidgets.QPushButton(self.profileInfoWidget)
        self.profileInfoSaveButton.setGeometry(QtCore.QRect(155, 227, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.profileInfoSaveButton.setFont(font)
        self.profileInfoSaveButton.setStyleSheet("#profileInfoSaveButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(5, 110, 0);\n"
"}\n"
"#profileInfoSaveButton:hover {\n"
"    border: 2px solid rgb(60, 62, 71);\n"
"    background-color: rgb(20, 135, 0);\n"
"}")
        self.profileInfoSaveButton.setObjectName("profileInfoSaveButton")
        self.profileTitle_2 = QtWidgets.QLabel(self.profileWidget)
        self.profileTitle_2.setGeometry(QtCore.QRect(60, 380, 210, 40))
        self.profileTitle_2.setObjectName("profileTitle_2")
        self.privacySettingsWidget = QtWidgets.QWidget(self.profileWidget)
        self.privacySettingsWidget.setGeometry(QtCore.QRect(50, 430, 310, 170))
        self.privacySettingsWidget.setStyleSheet("#privacySettingsWidget {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"}")
        self.privacySettingsWidget.setObjectName("privacySettingsWidget")
        self.privacySettingsLabel = QtWidgets.QLabel(self.privacySettingsWidget)
        self.privacySettingsLabel.setGeometry(QtCore.QRect(35, 10, 240, 30))
        self.privacySettingsLabel.setObjectName("privacySettingsLabel")
        self.publicButton = QtWidgets.QRadioButton(self.privacySettingsWidget)
        self.publicButton.setGeometry(QtCore.QRect(50, 54, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.publicButton.setFont(font)
        self.publicButton.setStyleSheet("")
        self.publicButton.setChecked(True)
        self.publicButton.setObjectName("publicButton")
        self.privateButton = QtWidgets.QRadioButton(self.privacySettingsWidget)
        self.privateButton.setGeometry(QtCore.QRect(180, 54, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.privateButton.setFont(font)
        self.privateButton.setStyleSheet("")
        self.privateButton.setObjectName("privateButton")
        self.privacySaveButton = QtWidgets.QPushButton(self.privacySettingsWidget)
        self.privacySaveButton.setGeometry(QtCore.QRect(70, 110, 161, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.privacySaveButton.setFont(font)
        self.privacySaveButton.setStyleSheet("#privacySaveButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(5, 110, 0);\n"
"}\n"
"#privacySaveButton:hover {\n"
"    border: 2px solid rgb(60, 62, 71);\n"
"    background-color: rgb(20, 135, 0);\n"
"}")
        self.privacySaveButton.setObjectName("privacySaveButton")
        self.profileBackButton = QtWidgets.QPushButton(self.profileWidget)
        self.profileBackButton.setGeometry(QtCore.QRect(20, 620, 160, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.profileBackButton.setFont(font)
        self.profileBackButton.setStyleSheet("#profileBackButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(5, 110, 0);\n"
"}\n"
"#profileBackButton:hover {\n"
"    border: 2px solid rgb(60, 62, 71);\n"
"    background-color: rgb(20, 135, 0);\n"
"}")
        self.profileBackButton.setObjectName("profileBackButton")
        self.aboutPrivacyWidget = QtWidgets.QWidget(self.profileWidget)
        self.aboutPrivacyWidget.setGeometry(QtCore.QRect(410, 470, 470, 180))
        self.aboutPrivacyWidget.setStyleSheet("#aboutPrivacyWidget {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"}")
        self.aboutPrivacyWidget.setObjectName("aboutPrivacyWidget")
        self.profileAboutLabel_1 = QtWidgets.QLabel(self.aboutPrivacyWidget)
        self.profileAboutLabel_1.setGeometry(QtCore.QRect(10, 10, 451, 31))
        self.profileAboutLabel_1.setObjectName("profileAboutLabel_1")
        self.profileAboutLabel_2 = QtWidgets.QLabel(self.aboutPrivacyWidget)
        self.profileAboutLabel_2.setGeometry(QtCore.QRect(20, 50, 410, 50))
        self.profileAboutLabel_2.setWordWrap(True)
        self.profileAboutLabel_2.setObjectName("profileAboutLabel_2")
        self.profileAboutLabel_3 = QtWidgets.QLabel(self.aboutPrivacyWidget)
        self.profileAboutLabel_3.setGeometry(QtCore.QRect(20, 110, 410, 50))
        self.profileAboutLabel_3.setWordWrap(True)
        self.profileAboutLabel_3.setObjectName("profileAboutLabel_3")
        self.horizontalLayout_3.addWidget(self.profileWidget)
        self.stackedWidget.addWidget(self.profilePage)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.profileFirstNameInput, self.profileLastNameInput)
        MainWindow.setTabOrder(self.profileLastNameInput, self.profileBirthdateInput)
        MainWindow.setTabOrder(self.profileBirthdateInput, self.profileCountryInput)
        MainWindow.setTabOrder(self.profileCountryInput, self.profileEmailInput)
        MainWindow.setTabOrder(self.profileEmailInput, self.profileInfoSaveButton)
        MainWindow.setTabOrder(self.profileInfoSaveButton, self.publicButton)
        MainWindow.setTabOrder(self.publicButton, self.privateButton)
        MainWindow.setTabOrder(self.privateButton, self.privacySaveButton)
        MainWindow.setTabOrder(self.privacySaveButton, self.profileBackButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt Music Archive"))
        self.menuTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">Main Menu</span></p></body></html>"))
        self.profileButtonTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Profile</span></p></body></html>"))
        self.profileButtonDescription.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Editing your profile &amp; account info. Privacy settings.</span></p></body></html>"))
        self.searchButtonTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Search</span></p></body></html>"))
        self.searchButtonDescription.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Search for content in the database, such as tracks, artists, albums, etc.</span></p></body></html>"))
        self.profileMainTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Anonymous</span></p></body></html>"))
        self.profileTitle_1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Profile &amp; Account Information</span></p></body></html>"))
        self.profileIconLabel_1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Your Profile Icon</span></p></body></html>"))
        self.profileIconLabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Change Icon</span></p></body></html>"))
        self.profileInfoLabel_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">First Name</span></p></body></html>"))
        self.profileInfoLabel_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Last Name</span></p></body></html>"))
        self.profileFirstNameInput.setPlaceholderText(_translate("MainWindow", "Ivan"))
        self.profileLastNameInput.setPlaceholderText(_translate("MainWindow", "Ivanov"))
        self.profileInfoLabel_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Country</span></p></body></html>"))
        self.profileBirthdateInput.setPlaceholderText(_translate("MainWindow", "01.01.1999"))
        self.profileInfoLabel_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Email</span></p></body></html>"))
        self.profileEmailInput.setPlaceholderText(_translate("MainWindow", "name@example.com"))
        self.profileInfoLabel_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Date of Birth</span></p></body></html>"))
        self.profileCountryInput.setPlaceholderText(_translate("MainWindow", "Russia"))
        self.profileInfoSaveButton.setText(_translate("MainWindow", "Save Data"))
        self.profileTitle_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Privacy Settings</span></p></body></html>"))
        self.privacySettingsLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Choose the type of your profile:</span></p></body></html>"))
        self.publicButton.setText(_translate("MainWindow", "Public"))
        self.privateButton.setText(_translate("MainWindow", "Private"))
        self.privacySaveButton.setText(_translate("MainWindow", "Save Data"))
        self.profileBackButton.setText(_translate("MainWindow", "Back to Main Menu"))
        self.profileAboutLabel_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">There is some information about profile types:</span></p></body></html>"))
        self.profileAboutLabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">- Public profile: other users can see all of your saved profile info.</span></p></body></html>"))
        self.profileAboutLabel_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">- Private profile: other users can see nothing but your username &amp; profile icon.</span></p></body></html>"))
from qwidget_clickable import QWidgetClickable
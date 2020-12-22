from PIL import Image

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap

from window import Window
from main_window_ui import Ui_MainWindow


class MainWindow(Window, Ui_MainWindow):
    def __init__(self, app):
        super().__init__(app)

    def setupButtons(self):
        self.toProfileButton.clicked.connect(self.toProfile)
        self.profileBackButton.clicked.connect(
            lambda: self.pageSwitch(self.stackedWidget, 0)
        )
        self.profileInfoSaveButton.clicked.connect(self.profileSaveInfo)
        self.privacySaveButton.clicked.connect(self.privacySaveInfo)
        self.changeIconButton.clicked.connect(self.profileChangeIcon)

    def toProfile(self):
        self.pageSwitch(self.stackedWidget, 1)
        user = self.sql_manager.get_user(self.app.getUser())
        self.profileMainTitle.setText(f'''<html><head/><body><p align="center">
        <span style=" font-size:36pt;">{self.app.getUser()}</span></p></body></html>
        ''')
        data = {
            'email': self.profileEmailInput,
            'first_name': self.profileFirstNameInput,
            'last_name': self.profileLastNameInput,
            'country': self.profileCountryInput,
            'date_of_birth': self.profileBirthdateInput
        }
        for key in data:
            data[key].setText(user[key])
        (self.publicButton if user['profile_type'] == 'public'
         else self.privateButton).setChecked(True)
        self.profileIconPic.setPixmap(QPixmap(user['icon_path']))

    def profileSaveInfo(self):
        update_data = {
            'email': self.profileEmailInput.text(),
            'first_name': self.profileFirstNameInput.text(),
            'last_name': self.profileLastNameInput.text(),
            'country': self.profileCountryInput.text(),
            'date_of_birth': self.profileBirthdateInput.text()
        }
        self.sql_manager.update_user(self.app.getUser(), update_data)

    def privacySaveInfo(self):
        profile_type = 'public' if self.publicButton.isChecked() else 'private'
        self.sql_manager.update_user(self.app.getUser(), {'profile_type': profile_type})

    def profileChangeIcon(self):
        source = QFileDialog.getOpenFileName(self, 'Select Image', '', "Image (*.png *.jpg *.jpeg)")[0]
        if not source:
            return
        destination = 'images/' + self.app.getUser() + '_icon.png'
        Image.open(source).save(destination)
        self.profileIconPic.setPixmap(QPixmap(destination))
        self.sql_manager.update_user(self.app.getUser(), {'icon_path': destination})

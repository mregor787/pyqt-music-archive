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
        self.toSearchButton.clicked.connect(self.toSearch)
        self.exitButton.clicked.connect(self.logout)
        for btn in [self.profileBackButton, self.searchBackButton,
                    self.artistBackButton, self.albumBackButton]:
            btn.clicked.connect(
                lambda: self.pageSwitch(self.stackedWidget, 0)
            )
        self.rulesBackButton.clicked.connect(self.toSearch)
        self.profileInfoSaveButton.clicked.connect(self.profileSaveInfo)
        self.privacySaveButton.clicked.connect(self.privacySaveInfo)
        self.changeIconButton.clicked.connect(self.profileChangeIcon)
        self.searchButton.clicked.connect(self.searchAction)
        self.searchAboutButton.clicked.connect(
            lambda: self.pageSwitch(self.stackedWidget, 3)
        )

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

    def toSearch(self):
        self.pageSwitch(self.stackedWidget, 2)

    def logout(self):
        self.app.setUser('')
        self.app.changeWindow('entry')

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

    @staticmethod
    def get_query_part_type(query_part: str, table: str) -> str:
        if len(set('><=') & set(query_part)) > 0:
            if table not in ['album', 'track']:
                return ''
            sign = ''.join(c for c in query_part if c in '><=')
            if sign not in ['=', '==', '>', '<', '>=', '<=']:
                return ''
            parameter, value = (x.strip() for x in query_part.split(sign))
            if parameter != 'year' and table == 'album':
                return ''
            if parameter not in ['year', 'duration', 'number']:
                return ''
            if not value.isdigit():
                return ''
            return 'parameter'
        return 'title'

    def get_query_part_data(self, query_part, table):
        data = []
        if query_part == '*':
            data = self.sql_manager.get_all_table_items(table)
        elif self.get_query_part_type(query_part, table) == 'title':
            data = self.sql_manager.get_table_items_by_partial_title(table, query_part)
        elif self.get_query_part_type(query_part, table) == 'parameter':
            sign = ''.join(c for c in query_part if c in '><=')
            parameter, value = (x.strip() for x in query_part.split(sign))
            data = self.sql_manager.get_table_items_by_parameter(
                table, parameter, int(value), sign
            )
        return data

    def searchAction(self):
        self.setFocus()
        query = self.searchInput.text().strip()
        if not query:
            return
        table = self.searchComboBox.currentText()[:-1].lower()
        data = []
        if '&' in query:
            query_parts = [part.strip() for part in query.split('&')]
            for part in query_parts:
                if not self.get_query_part_type(part, table):
                    return
            for i, part in enumerate(query_parts):
                part_data = self.get_query_part_data(part, table)
                if i == 0:
                    data = part_data
                else:
                    data = [item for item in data if item in part_data]
        else:
            data = self.get_query_part_data(query, table)
        print(data)

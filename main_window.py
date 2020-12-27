from PIL import Image

from PyQt5.QtWidgets import QFileDialog, QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QPixmap

from qwidget_clickable import QWidgetClickable
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
        self.addDataToScrollArea(data, table, self.searchScrollArea)

    def addDataToScrollArea(self, data, table, scroll_area):
        box = scroll_area.widget()
        for obj in box.findChildren(QWidget):
            for child in obj.children():
                child.deleteLater()
            obj.deleteLater()
        for i, item in enumerate(data):
            new_widget = QWidgetClickable(box)
            name = f'search{table.capitalize()}Widget_{i + 1}'
            new_widget.setObjectName(name)
            new_widget.setMinimumHeight(80)
            new_widget.setMaximumHeight(80)
            table_colors = {
                'artist': ('rgb(192, 57, 43)', 'rgb(231, 76, 60)'),
                'album': ('rgb(41, 128, 185)', 'rgb(52, 152, 219)'),
                'track': ('rgb(39, 174, 96)', 'rgb(46, 204, 113)'),
                'genre': ('rgb(142, 68, 173)', 'rgb(155, 89, 182)')
            }
            new_widget.setStyleSheet(f'''
            #{name} {{
                border: 2px solid rgb(37, 39, 48);
                border-radius: 10px;
                background-color: {table_colors[table][0]};
            }}
            #{name}:hover {{
                border: 2px solid rgb(60, 62, 71);
                background-color: {table_colors[table][1]};
            }}''')
            box.findChild(QVBoxLayout).addWidget(new_widget)
            logo = QLabel(new_widget)
            logo.setGeometry(10, 10, 60, 60)
            path = 'images/logo/'
            if table == 'track':
                artist = self.sql_manager.get_artist_by_track(item["title"])[0]["name"].lower()
                if item['album'] is not None:
                    album = self.sql_manager.get_album_by_track(item["title"])[0]["title"].lower()
                    path += f'album/{artist}_{album}.png'
                else:
                    path += f'artist/{artist}.png'
            elif table == 'album':
                artist = self.sql_manager.get_artist_by_album(item["title"])[0]["name"].lower()
                path += f'album/{artist}_{item["title"].lower()}.png'
            else:
                path += f'{table}/{item["name"].lower()}.png'
            logo.setPixmap(QPixmap(path))
            logo.setScaledContents(True)
            title = QLabel(new_widget)
            title.setGeometry(75, 10, 415, 60)
            text = item['name' if table in ['artist', 'genre'] else 'title']
            title.setText(f'''<html><head/><body><p>
            <span style=" font-size:14pt;">{text}</span></p></body></html>
            ''')

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from sql_manager import SqlManager
from entry import Entry


class Application:
    def __init__(self):
        self.sql_manager = SqlManager('music.db')
        self.current_window = Entry(self)
        self.current_window.show()
        self.centerCurrentWindow()

    def changeWindow(self, window: QMainWindow):
        self.current_window.close()
        self.current_window = window
        self.current_window.show()
        self.centerCurrentWindow()

    def centerCurrentWindow(self):
        window = self.current_window
        frame_geometry = window.frameGeometry()
        desktop = QApplication.desktop()
        screen = desktop.screenNumber(desktop.cursor().pos())
        center_point = desktop.screenGeometry(screen).center()
        frame_geometry.moveCenter(center_point)
        window.move(frame_geometry.topLeft())


def main():
    app = QApplication(sys.argv)
    my_app = Application()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

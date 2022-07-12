import sys

from PyQt5.QtWidgets import QApplication

from widgets.main_window import MainWindow
from style import STYLE

import widgets


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

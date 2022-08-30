import os
import sys

from PyQt5.QtWidgets import QApplication

from widgets.main_window import MainWindow
from style import STYLE

import widgets


def on_startup() -> None:
    """Создает папку для результатов шифрования, если таковой нет"""
    if not os.path.exists(os.path.join(os.getcwd(), 'data')):
        os.mkdir('data')


def main():
    on_startup()
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

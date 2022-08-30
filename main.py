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


def process_haffman(string: str):
    res = ""
    for sym in string:
        tmp = str(((ord(sym) + 7) * 15) - 4)
        value = '0' * (5 - len(tmp)) + tmp
        res += value
    return res


def decrypt_haffman(string: str):
    res = ""
    for i in range(0, len(string), 5):
        tmp = int(string[i:i+5])
        value = chr((tmp + 4) // 15 - 7)
        res += value
    return res


if __name__ == '__main__':
    main()

from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QApplication, QPushButton, QLabel
from PyQt5.Qt import QRect


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setMinimumSize(1280, 720)
        rect = QRect(QApplication.desktop().width() - self.width() // 2,
                     QApplication.desktop().height() - self.height() // 2,
                     self.width(), self.height())
        self.setGeometry(rect)
        self.init_ui()

    def init_ui(self):
        left_top_btn = QPushButton("Push me")
        right_top_text = QLabel("Hello, world!")
        left_bottom_btn = QPushButton("Don't push me")
        right_bottom_text = QLabel("Good day!")

        layout = QGridLayout()

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(layout)

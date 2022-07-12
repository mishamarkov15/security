from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QApplication, QPushButton, QLabel
from PyQt5.Qt import QRect

from widgets.upload_file import UploadFile
from widgets.algorithm_select import AlgorithmWidget
from widgets.process_file import ProcessAlgorithm


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.left_widget = None
        self.central_widget = None
        self.right_widget = None
        self.setMinimumSize(1280, 720)
        rect = QRect(QApplication.desktop().width() - self.width() // 2,
                     QApplication.desktop().height() - self.height() // 2,
                     self.width(), self.height())
        self.setGeometry(rect)
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        self.left_widget = UploadFile(self)
        self.central_widget = AlgorithmWidget(self)
        self.right_widget = ProcessAlgorithm(self)
        layout.addWidget(self.left_widget, 0, 0)
        layout.addWidget(self.central_widget, 0, 1)
        layout.addWidget(self.right_widget, 0, 2)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(layout)

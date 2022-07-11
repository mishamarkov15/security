import os.path

from PyQt5.QtWidgets import QWidget, QGridLayout, QFileDialog, QPushButton, QLabel, QTextEdit
import PyQt5.Qt


class UploadFile(QWidget):

    def __init__(self, parent=None):
        super(UploadFile, self).__init__(parent)
        self.upload_button = None
        self.title = None
        self.file_name_title = None
        self.layout = None
        self.init_ui()

    def init_ui(self):
        self.layout = QGridLayout()

        self.title = QLabel("Выберите файл")

        self.file_name_title = QTextEdit("Файл не выбран")
        self.file_name_title.setReadOnly(True)

        self.upload_button = QPushButton()
        self.upload_button.setText("Выбрать файл")
        self.upload_button.setMinimumSize(100, 100)
        self.upload_button.clicked.connect(self.select_file)

        self.layout.addWidget(self.upload_button, 4, 1, 1, 1)
        self.layout.addWidget(self.title, 0, 0, 1, 3)
        self.layout.addWidget(self.file_name_title, 1, 0, 1, 3)

        self.setLayout(self.layout)

    def select_file(self):
        file_path = os.path.basename(QFileDialog().getOpenFileName()[0])
        self.file_name_title.setText(file_path)

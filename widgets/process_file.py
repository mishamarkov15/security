import os.path
import hashlib

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton

from PyQt5.QtCore import Qt
from cryptography.fernet import Fernet

import widgets.upload_file


class ProcessAlgorithm(QWidget):

    def __init__(self, parent=None):
        super(ProcessAlgorithm, self).__init__(parent)
        self.key = None
        self.layout = None
        self.file_title = None
        self.algo_title = None
        self.selected_file = None
        self.selected_algo = None
        self.crypto_button = None
        self.init_ui()
        self.setDisabled(True)

    def init_ui(self):
        layout = QGridLayout()

        self.file_title = QLabel("Выбранный файл:")
        self.file_title.setMaximumHeight(self.file_title.font().pointSize() * 3)
        self.file_title.setAlignment(Qt.AlignLeft)

        self.algo_title = QLabel("Выбранный алгоритм:")
        self.algo_title.setMaximumHeight(self.algo_title.font().pointSize() * 3)
        self.algo_title.setAlignment(Qt.AlignLeft)

        self.selected_file = QLabel("")
        self.selected_file.setMaximumHeight(self.selected_file.font().pointSize() * 3)
        self.selected_file.setAlignment(Qt.AlignLeft)

        self.selected_algo = QLabel("")
        self.selected_algo.setMaximumHeight(self.selected_algo.font().pointSize() * 3)
        self.selected_algo.setAlignment(Qt.AlignLeft)

        self.crypto_button = QPushButton("Зашифровать")
        self.crypto_button.setMinimumSize(100, 50)
        self.crypto_button.clicked.connect(self.process_algorithm)

        layout.addWidget(self.file_title, 0, 0, 1, 1)
        layout.addWidget(self.algo_title, 1, 0, 1, 1)
        layout.addWidget(self.selected_file, 0, 1, 1, 1)
        layout.addWidget(self.selected_algo, 1, 1, 1, 1)
        layout.addWidget(self.crypto_button, 3, 0, 1, 2)

        self.setLayout(layout)

    @staticmethod
    def write_key():
        key = Fernet.generate_key()
        with open('crypto.key', 'wb') as file:
            file.write(key)

    def load_key(self):
        self.key = open('crypto.key', 'rb').read()

    def process_algorithm(self):
        file_path = self.parent().findChild(widgets.upload_file.UploadFile).full_file_path

        if self.algo_title == 'AES':
            if not os.path.exists(os.path.join(os.getcwd(), 'crypto.key')):
                ProcessAlgorithm.write_key()
                self.load_key()
            f = Fernet(self.key)
            with open(file_path, 'rb') as file:
                file_data = file.read()
                encrypted_data = f.encrypt(file_data)
            with open('result.txt', 'wb') as file:
                file.write(encrypted_data)
        else:
            with open(file_path, 'rb') as file:
                with open('result.txt', 'w') as output_file:
                    for line in file.readlines():
                        hashed_line = hashlib.sha256(line.rstrip()).hexdigest()
                        output_file.write(hashed_line + '\n')

    def setDisabled(self, a0: bool) -> None:
        super(ProcessAlgorithm, self).setDisabled(a0)
        if self.isEnabled():
            file_name = self.parent().findChild(widgets.upload_file.UploadFile).file_name_title.text()
            self.selected_file.setText(file_name)

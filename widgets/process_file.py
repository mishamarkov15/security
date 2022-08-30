import os.path
import hashlib

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QMessageBox, QInputDialog

from PyQt5.QtCore import Qt
from cryptography.fernet import Fernet

import widgets.upload_file

PATH_TO_RESULT = os.path.join(os.getcwd(), 'data')


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
        self.decrypt_button = None
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

        self.decrypt_button = QPushButton("Расшифровать")
        self.decrypt_button.setMinimumSize(100, 50)
        self.decrypt_button.clicked.connect(self.decrypt_algorithm)

        layout.addWidget(self.file_title, 0, 0, 1, 1)
        layout.addWidget(self.algo_title, 1, 0, 1, 1)
        layout.addWidget(self.selected_file, 0, 1, 1, 1)
        layout.addWidget(self.selected_algo, 1, 1, 1, 1)
        layout.addWidget(self.crypto_button, 3, 0, 1, 1)
        layout.addWidget(self.decrypt_button, 3, 1, 1, 1)

        self.setLayout(layout)

    def write_key(self):
        key = Fernet.generate_key()
        with open(os.path.join(PATH_TO_RESULT + 'crypto.key'), 'wb') as file:
            file.write(key)
        with open(os.path.join(PATH_TO_RESULT + f'{self.selected_file.text()}_crypto_key.txt'), 'wb') as file:
            file.write(key)

    def load_key(self):
        self.key = open(PATH_TO_RESULT + 'crypto.key', 'rb').read()

    def process_AES(self, file_path: str):
        """Шифрование алгоритмом AES"""
        if not os.path.exists(os.path.join(PATH_TO_RESULT, 'crypto.key')):
            ProcessAlgorithm.write_key(self)
            self.load_key()
        f = Fernet(self.key)
        print(self.key)
        with open(file_path, 'rb') as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
        with open(os.path.join(PATH_TO_RESULT, 'result_AES.txt'), 'wb') as file:
            file.write(encrypted_data)

    def decrypt_AES(self, file_path: str, secret_code: str):
        """Расшифровка AES алгоритма"""
        self.key = secret_code
        f = Fernet(self.key)
        with open(file_path, 'rb') as file:
            file_data = file.read()
            decrypted_data = f.decrypt(file_data)
        with open(os.path.join(PATH_TO_RESULT, f'decrypted_AES.txt'), 'wb') as file:
            file.write(decrypted_data)

    @staticmethod
    def process_caesar(file_path: str):
        """Шифрование алгоритмом Цезаря"""
        with open(file_path, 'r') as file:
            data = file.read()
        with open(os.path.join(PATH_TO_RESULT, 'result_caesar.txt'), 'w') as file:
            result = ''
            for sym in data:
                try:
                    if sym.isalnum():
                        result += '111' + chr(ord(sym) - 13)
                    else:
                        result += '000' + sym
                except ValueError as error:
                    result += '000' + sym
            file.write(result)

    @staticmethod
    def decrypt_caesar(file_path: str):
        """Расшифровка алгоритма цезаря"""
        with open(file_path, 'r') as file:
            data = file.read()
        with open(os.path.join(PATH_TO_RESULT, 'decrypted_caesar.txt'), 'w') as file:
            result = ''
            for i in range(0, len(data) - 4, 4):
                if data[i:i+4].startswith('111'):
                    result += chr(ord(data[i+3]) + 13)
                else:
                    result += data[i + 3]
            file.write(result)

    @staticmethod
    def process_haffman(file_path: str):
        """Шифр Хаффмана"""
        with open(file_path, 'r') as file:
            data = file.read()
        res = ""
        for sym in data:
            tmp = str(((ord(sym) + 7) * 15) - 4)
            value = '0' * (5 - len(tmp)) + tmp
            res += value
        with open(os.path.join(PATH_TO_RESULT, 'result_Haffman.txt'), 'w') as file:
            file.write(res)

    @staticmethod
    def decrypt_haffman(file_path: str):
        """Рашифровка Хаффмана"""
        with open(file_path, 'r') as file:
            data = file.read()
        res = ""
        for i in range(0, len(data), 5):
            tmp = int(data[i:i + 5])
            value = chr((tmp + 4) // 15 - 7)
            res += value
        with open(os.path.join(PATH_TO_RESULT, 'decrypted_Haffman.txt'), 'w') as file:
            file.write(res)

    def process_algorithm(self):
        file_path = self.parent().findChild(widgets.upload_file.UploadFile).full_file_path
        msg = QMessageBox(self)
        msg.setWindowTitle("Успешно!")
        msg.setStandardButtons(QMessageBox.Ok)

        if self.selected_algo.text() == 'AES':
            self.process_AES(file_path)
            msg.setText(f"Файл успешно зашифрован. Результат записан в "
                        f"{'result_' + self.selected_algo.text() + '.txt'}.\n"
                        f"Для расшифрования Вам потребуется ключ, который"
                        f" записан в файл {self.selected_file.text()}_crypto_key_{self.selected_algo.text()}.txt.")
        elif self.selected_algo.text() == "Caesar's algorithm":
            self.process_caesar(file_path)
            msg.setText(f"Файл успешно зашифрован. Результат записан в result_caesar.txt.")
        elif self.selected_algo.text() == "Huffman algorithm":
            self.process_haffman(file_path)
            msg.setText(f"Файл успешно зашифрован. Результат записан в result_Haffman.txt.")
        else:
            with open(file_path, 'rb') as file:
                with open('result_SHA-256.txt', 'w') as output_file:
                    for line in file.readlines():
                        hashed_line = hashlib.sha256(line.rstrip()).hexdigest()
                        output_file.write(hashed_line + '\n')
        msg.show()

    def decrypt_algorithm(self) -> None:
        file_path = self.parent().findChild(widgets.upload_file.UploadFile).full_file_path
        algo_name = ''

        if self.selected_algo.text() == "AES":
            text, ok = QInputDialog.getText(self, 'Ключ для расшифровки', 'Введите ключ для расшифровки')
            if ok and len(text) > 0:
                print(text)
            else:
                return
            self.decrypt_AES(file_path, text)
            algo_name = "AES"
        elif self.selected_algo.text() == "SHA-256":
            print("Decrypting with SHA-256")
            algo_name = "AES"
        elif self.selected_algo.text() == "Caesar's algorithm":
            self.decrypt_caesar(file_path)
            algo_name = "caesar"
        elif self.selected_algo.text() == "Huffman algorithm":
            self.decrypt_haffman(file_path)
            algo_name = "Haffman"

        msg = QMessageBox(self)

        msg.setText(f"Файл успешно расшиврован. Результат записан в {'decrypted_' + algo_name}.txt")
        msg.setWindowTitle("Успешно")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()

    def setDisabled(self, a0: bool) -> None:
        super(ProcessAlgorithm, self).setDisabled(a0)
        if self.isEnabled():
            file_name = self.parent().findChild(widgets.upload_file.UploadFile).file_name_title.text()
            self.selected_file.setText(file_name)

import os.path

from PyQt5.QtWidgets import QWidget, QGridLayout, QFileDialog, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt

import widgets.algorithm_select


class UploadFile(QWidget):

    def __init__(self, parent=None):
        super(UploadFile, self).__init__(parent)
        self.full_file_path = None
        self.upload_button = None
        self.title = None
        self.file_name_title = None
        self.layout = None
        self.init_ui()

    def init_ui(self):
        self.layout = QGridLayout()

        self.title = QLabel("Выберите файл")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setMaximumHeight(self.title.font().pointSize() * 3)

        self.file_name_title = QLineEdit("Файл не выбран")
        self.file_name_title.setReadOnly(True)
        self.file_name_title.setTextMargins(10, 10, 10, 10)

        self.upload_button = QPushButton()
        self.upload_button.setText("Выбрать файл")
        self.upload_button.setMinimumSize(100, 50)
        self.upload_button.clicked.connect(self.select_file)

        self.layout.addWidget(self.title, 0, 0, 1, 3)
        self.layout.addWidget(self.file_name_title, 1, 0, 1, 3)
        self.layout.addWidget(QWidget(), 2, 0, 2, 3)
        self.layout.addWidget(self.upload_button, 4, 0, 1, 1)

        self.setLayout(self.layout)

    def select_file(self):
        file_path = QFileDialog().getOpenFileName()[0]
        self.full_file_path = os.path.join(file_path)
        self.file_name_title.setText(os.path.basename(file_path))
        self.parent().findChild(widgets.algorithm_select.AlgorithmWidget).setDisabled(False)

        #right_widget = self.parent().findChild(widgets.algorithm_select.AlgorithmWidget)
        #if right_widget.isEnabled():
            #right_widget.selected_algo.setText(self.file_name_title)

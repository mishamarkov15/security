from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QRadioButton

from PyQt5.QtCore import Qt

import widgets.process_file


class AlgorithmWidget(QWidget):

    def __init__(self, parent=None):
        super(AlgorithmWidget, self).__init__(parent)
        self.layout = None
        self.title = None
        self.active_button = None
        self.init_ui()
        self.setDisabled(True)

    def init_ui(self):
        layout = QGridLayout()

        self.title = QLabel("Выберите алгоритм")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setMaximumHeight(self.title.font().pointSize() * 3)

        algo_1 = QRadioButton("AES")
        algo_1.setObjectName("AES")
        algo_1.toggled.connect(self.on_clicked)

        algo_2 = QRadioButton("Шифр Джосефа")
        algo_2.setObjectName("Josephus algorithm")
        algo_2.toggled.connect(self.on_clicked)

        algo_3 = QRadioButton("Шифр Цезаря")
        algo_3.setObjectName("Caesar's algorithm")
        algo_3.toggled.connect(self.on_clicked)

        algo_4 = QRadioButton("Шифр Хаффмана")
        algo_4.setObjectName("Huffman algorithm")
        algo_4.toggled.connect(self.on_clicked)

        layout.addWidget(self.title, 1, 1, 1, 3)
        layout.addWidget(algo_1, 2, 1, 1, 3)
        layout.addWidget(algo_2, 3, 1, 1, 3)
        layout.addWidget(algo_3, 4, 1, 1, 3)
        layout.addWidget(algo_4, 5, 1, 1, 3)
        layout.addWidget(QWidget(), 0, 4, 7, 1)

        self.setLayout(layout)

    def on_clicked(self):
        btn = self.sender()

        right_widget = self.parent().findChild(widgets.process_file.ProcessAlgorithm)
        if not right_widget.isEnabled():
            right_widget.setDisabled(False)

        if btn.isChecked():
            self.active_button = btn
            right_widget.selected_algo.setText(self.active_button.objectName())


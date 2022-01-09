from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit


class Scribe(QWidget):
    def __init__(self):
        super().__init__()

        text_edit = QTextEdit()

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(text_edit)
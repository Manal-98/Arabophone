import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    edit = QTextEdit()
    mainWindow.setCentralWidget(edit)
    mainWindow.resize(800, 600)
    mainWindow.show()
    sys.exit(app.exec_())

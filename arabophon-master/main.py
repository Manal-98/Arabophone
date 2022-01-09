import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from dashboard import Dashboard

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    mainWindow.resize(800, 600)
    dashboard = Dashboard()
    mainWindow.setCentralWidget(dashboard)
    mainWindow.show()
    sys.exit(app.exec_())
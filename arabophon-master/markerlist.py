from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem


class MarkerList(QListWidget):
    def __init__(self, select):
        super().__init__()
        self.__select = select
        self.itemClicked.connect(self.__on_item_clicked)

    def add_marker(self, marker):
        name = 'Marker ' + str(self.count())
        item = QListWidgetItem(name)
        item.setData(Qt.UserRole, marker)
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.addItem(item)

    def __on_item_clicked(self, item):
        marker = item.data(Qt.UserRole)
        self.__select(marker)
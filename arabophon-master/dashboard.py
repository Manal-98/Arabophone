from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QComboBox

from externalizer import Externalizer
from scribe import Scribe
from waveplot import WavePlot
from sound import Sound
from markerlist import MarkerList


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.__sound = None
        self.__scribe = Scribe()
        self.__waveplot = WavePlot()

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        upper_layout = QHBoxLayout()
        main_layout.addLayout(upper_layout)

        load_button = QPushButton('Load')
        upper_layout.addWidget(load_button)
        load_button.clicked.connect(self.__on_click_load_button)

        play_button = QPushButton('Play')
        upper_layout.addWidget(play_button)
        play_button.clicked.connect(self.__on_click_play_button)

        play_selection_button = QPushButton('Play selection')
        upper_layout.addWidget(play_selection_button)
        play_selection_button.clicked.connect(
            self.__on_click_play_selection_button)

        mark_button = QPushButton('Mark')
        upper_layout.addWidget(mark_button)
        mark_button.clicked.connect(self.__on_click_mark_button)

        self.__combo = QComboBox()
        self.__combo.addItem('Neutral')
        self.__combo.addItem('Happiness')
        self.__combo.addItem('Sadness')
        self.__combo.addItem('Anger')
        self.__combo.addItem('Fear')
        upper_layout.addWidget(self.__combo)

        export_button = QPushButton('Export')
        upper_layout.addWidget(export_button)
        export_button.clicked.connect(self.__on_click_export_button)

        lower_layout = QHBoxLayout()
        main_layout.addLayout(lower_layout)

        left_layout = QVBoxLayout()
        lower_layout.addLayout(left_layout)

        self.__marker_list = MarkerList(self.__select_marker)
        left_layout.addWidget(self.__marker_list)

        right_layout = QVBoxLayout()
        lower_layout.addLayout(right_layout)
        right_layout.addWidget(self.__scribe)
        right_layout.addWidget(self.__waveplot)

    def load(self, filename):
        self.__sound = Sound(filename)
        self.__waveplot.load(self.__sound)

    def __select_marker(self, marker):
        self.__waveplot.select_marker(marker)
        self.__combo.setCurrentText(marker.label())

    def __on_click_load_button(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if len(filenames) == 1:
                filename = filenames[0]
                self.load(filename)

    def __on_click_play_selection_button(self):
        limits = self.__waveplot.curve().selection().limits()
        if limits:
            self.__sound.play_interval(*limits)

    def __on_click_play_button(self):
        self.__sound.play()

    def __on_click_mark_button(self):
        marker = self.__waveplot.create_marker(self.__combo.currentText())
        self.__marker_list.add_marker(marker)

    def __on_click_export_button(self):
        limits = self.__waveplot.curve().selection().limits()
        if limits:
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.DirectoryOnly)
            if dialog.exec():
                directories = dialog.selectedFiles()
                if len(directories) == 1:
                    directory = directories[0]
                    externalizer = Externalizer(directory)
                    externalizer.externalize(self.__sound, limits, self.__combo.currentText())

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from waveplot import WavePlot
from sound import Sound


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        sound = Sound()
        waveplot = WavePlot(sound)
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(waveplot.widget())
        waveplot.draw()
        sound.play()
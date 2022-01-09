from PyQt5.QtWidgets import QWidget, QVBoxLayout

from curve import Curve
from marker import Marker
from spectrogram import Spectrogram


class WavePlot(QWidget):
    def __init__(self):
        super().__init__()

        self.__sound = None

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.__curve = Curve(self.__select)
        layout.addWidget(self.__curve)

        self.__spectrogram = Spectrogram()
        layout.addWidget(self.__spectrogram)

    def load(self, sound):
        self.__sound = sound
        self.__curve.load(self.__sound)
        self.__spectrogram.load(self.__sound)

    def curve(self):
        return self.__curve

    def spectrogram(self):
        return self.__spectrogram

    def create_marker(self, label):
        limits = self.__curve.selection().limits()
        if not limits:
            return None
        return Marker(limits, label)

    def select_marker(self, marker):
        self.__curve.selection().set_limits(marker.limits())

    def __select(self, x0, x1):
        self.__sound.play_interval(x0, x1)
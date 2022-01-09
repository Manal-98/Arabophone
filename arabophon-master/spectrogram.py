from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Spectrogram(QWidget):
    def __init__(self):
        super().__init__()

        self.__sound = None

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.__figure = Figure()
        self.__canvas = FigureCanvas(self.__figure)
        layout.addWidget(self.__canvas)
        self.__figure.tight_layout(pad=5)
        self.__subplot = self.__figure.add_subplot(1, 1, 1)
        self.__subplot.set_xlabel('Time', fontsize=10)
        self.__subplot.set_ylabel('Frequency', fontsize=10)

    def load(self, sound):
        self.__sound = sound
        self.__subplot.specgram(sound.s(), Fs=sound.rate(), cmap='jet')
        self.refresh()

    def refresh(self):
        self.__figure.canvas.draw()
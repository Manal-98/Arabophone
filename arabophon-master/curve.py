from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from selection import Selection


class Curve(QWidget):
    def __init__(self, select):
        super().__init__()

        self.__sound = None

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.__figure, self.__ax = pyplot.subplots(nrows=1, ncols=1)

        canvas = FigureCanvas(self.__figure)
        layout.addWidget(canvas)
        self.__figure.tight_layout(pad=5)
        self.__ax.set_xlabel('Time', fontsize=10)
        self.__ax.set_ylabel('Wave', fontsize=10)

        self.__selection = Selection(self.__ax.figure, select)
        self.__ax.add_patch(self.__selection)

    def load(self, sound):
        self.__sound = sound
        self.__ax.plot(sound.t(), sound.s(), '-', color='b')
        self.__selection.load(sound)
        self.refresh()

    def refresh(self):
        self.__figure.canvas.draw()

    def selection(self):
        return self.__selection
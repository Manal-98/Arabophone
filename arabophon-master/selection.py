from matplotlib.patches import Rectangle


class Selection(Rectangle):
    def __init__(self, figure, select):
        super().__init__((0, 0), 0, 0, figure=figure, zorder=1000)
        self.__select = select
        self.__figure = figure
        self.__sound = None
        self.__x0 = None
        self.__y0 = None
        self.__x1 = None
        self.__y1 = None
        self.set_alpha(0.5)
        figure.canvas.mpl_connect('button_press_event', self.__on_press)
        figure.canvas.mpl_connect('button_release_event', self.__on_release)

    def load(self, sound):
        self.__sound = sound

    def limits(self):
        if self.__x0 and self.__x1:
            return self.__x0, self.__x1
        return None

    def set_limits(self, limits):
        if limits:
            self.__x0, self.__x1 = limits
            self.refresh()

    def refresh(self):
        if self.__sound is None:
            return
        self.__y0 = self.__sound.s_min()
        self.__y1 = self.__sound.s_max()
        self.set_xy((self.__x0, self.__y0))
        self.set_width(self.__x1 - self.__x0)
        self.set_height(self.__y1 - self.__y0)
        self.__figure.canvas.draw()

    def __on_press(self, event):
        self.__x0 = event.xdata

    def __on_release(self, event):
        self.__x1 = event.xdata
        self.__x0, self.__x1 = sorted([self.__x0, self.__x1])
        self.refresh()
        self.__select(self.__x0, self.__x1)
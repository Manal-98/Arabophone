class Marker:
    def __init__(self, limits, label):
        self.__limits = limits
        self.__label = label

    def limits(self):
        return self.__limits

    def label(self):
        return self.__label

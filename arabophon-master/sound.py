import numpy
import os
from scipy.io import wavfile as wav
import simpleaudio as sa


class Sound:
    def __init__(self, filename):
        self.__filename = os.path.abspath(filename)
        self.__rate, self.__s = wav.read(self.__filename)
        self.__dt = 1 / self.__rate
        self.__duration = self.__dt * len(self.__s)
        self.__t = numpy.linspace(0, self.__duration, len(self.__s))
        self.__s_min = int(numpy.min(self.__s))
        self.__s_max = int(numpy.max(self.__s))

    def filename(self):
        return self.__filename

    def rate(self):
        return self.__rate

    def s(self):
        return self.__s

    def s_min(self):
        return self.__s_min

    def s_max(self):
        return self.__s_max

    def dt(self):
        return self.__dt

    def duration(self):
        return self.__duration

    def t(self):
        return self.__t

    def play(self):
        wave_obj = sa.WaveObject.from_wave_file(self.__filename)
        wave_obj.num_channels = 1
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def play_interval(self, t0, t1):
        i0 = 2 * int(t0 / self.__dt)
        i1 = 2 * int(t1 / self.__dt)
        wave_obj = sa.WaveObject.from_wave_file(self.__filename)
        wave_obj.num_channels = 1
        wave_obj.audio_data = wave_obj.audio_data[i0:i1]
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def export_interval(self, filename, t0, t1):
        i0 = int(t0 / self.__dt)
        i1 = int(t1 / self.__dt)
        wav.write(filename, self.__rate, self.__s[i0:i1])

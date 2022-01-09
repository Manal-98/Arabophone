import os
from datetime import datetime


class Externalizer:
    def __init__(self, directory):
        self.__directory = directory

    def externalize(self, sound, limits, label):
        uid = self.__generate_uid()
        self.__export_data(uid, sound, limits)
        self.__export_meta(uid, label)

    @staticmethod
    def __generate_uid():
        uid = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return uid

    def __export_data(self, uid, sound, limits):
        # Export sound interval to data/uid.csv
        data_directory = os.path.join(self.__directory, 'data')
        if not os.path.isdir(data_directory):
            os.mkdir(data_directory)
        filename = os.path.join(data_directory, uid + '.wav')
        sound.export_interval(filename, *limits)

    def __export_meta(self, uid, label):
        # Export pair (uid,label) to meta/base.csv
        meta_directory = os.path.join(self.__directory, 'meta')
        if not os.path.isdir(meta_directory):
            os.mkdir(meta_directory)
        filename = os.path.join(meta_directory, 'base.csv')
        if not os.path.isfile(filename):
            with open(filename, 'w') as f:
                f.write('uid;label\n')
        with open(filename, 'a') as f:
            f.write(uid + '.wav' + ';' + label + '\n')

import matplotlib.pyplot as plot
from scipy.io import wavfile

rate, data = wavfile.read('bonjour.wav')
print(rate)

plot.subplot(211)
plot.plot(data)
plot.xlabel('Sample')
plot.ylabel('Amplitude')

plot.subplot(212)
plot.specgram(data, Fs=rate, cmap='jet')
plot.xlabel('Time')
plot.ylabel('Frequency')

plot.show()

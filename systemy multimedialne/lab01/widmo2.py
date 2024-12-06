import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import scipy.fftpack

from zad2 import plotAudio

#data, fs = sf.read('sin_440Hz.wav', dtype=np.int32)

#fsize=2**8

#plt.figure()
#plt.subplot(2,1,1)
#plt.plot(np.arange(0,data.shape[0])/fs,data)

#plt.subplot(2,1,2)
#yf = scipy.fftpack.fft(data,fsize)
#plt.plot(np.arange(0,fs/2,fs/fsize),20*np.log10( np.abs(yf[:fsize//2])))
#plt.show()

# Wczytaj plik audio
signal, fs = sf.read('sin_440Hz.wav')

# Wywołaj funkcję
plotAudio(signal, fs, TimeMargin=[0.1, 0.2])
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import scipy.fftpack

data, fs = sf.read('sound1.wav', dtype='float32')

print(data.dtype)
print(data.shape)

#plt.subplot(2,1,1)
#plt.plot(data[:,0])
#plt.title('Lewy kanał')

#plt.subplot(2,1,2)
#plt.plot(data[:,1])
#plt.title('Prawy kanał')

time = np.linspace(0, len(data) / fs, len(data))

plt.subplot(2,1,1)
plt.plot(time, data[:,0])
plt.title('Lewy kanał')

plt.subplot(2,1,2)
plt.plot(time, data[:,1])
plt.title('Prawy kanał')

plt.show()
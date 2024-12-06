import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf

data, fs = sf.read('sound1.wav', dtype='float32')

print(data.dtype)
print(data.shape)

sf.write('sound_L.wav', data[:,0],fs)
sf.write('sound_R.wav', data[:,1],fs)

dataL, fsL = sf.read('sound_L.wav', dtype='float32')
dataR, fsR = sf.read('sound_R.wav', dtype='float32')

dataM=(dataL+dataR)/2

sf.write('sound_mix.wav', dataM,fs)
dataM, fsM = sf.read('sound_mix.wav', dtype='float32')

sd.play(data, fs)
status = sd.wait()
sd.play(dataL, fsL)
status1 = sd.wait()
sd.play(dataR, fsR)
status2 = sd.wait()
sd.play(dataM, fsM)
status3 = sd.wait()
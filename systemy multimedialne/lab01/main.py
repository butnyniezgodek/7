import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf

data, fs = sf.read('sound1.wav', dtype='float32')

print(data.dtype)
print(data.shape)

print(data)

sd.play(data, fs)
status = sd.wait()
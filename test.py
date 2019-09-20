import scipy.io.wavfile
import numpy as np
Fs, y_input = scipy.io.wavfile.read('test.wav')
print(len(y_input))
zero1 = np.zeros((len(y_input)),dtype=np.int16)
print(Fs)
print(y_input)


d1 = np.c_[y_input,y_input,y_input,y_input,y_input,y_input,zero1,zero1]
print(d1)
d1.dtype="int16"
print(d1.dtype)
print(y_input.shape)
print(zero1.shape)

scipy.io.wavfile.write("out.pcm",16000,d1)

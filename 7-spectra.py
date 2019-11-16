import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


t = np.linspace(0.0, 10, 5001)
sig = signal.chirp(t, f0=1, t1=10, f1=30, method='linear')
plt.figure()
plt.plot(t, sig)
plt.title("Signal in time domain")

plt.figure()
fs = 5001.0/10.0
f, t, Sxx = signal.spectrogram(sig, fs, nfft=2048, nperseg=128)

plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency')
plt.xlabel('Time')
plt.ylim((0,30))
plt.title("Spectrogram")
plt.show()


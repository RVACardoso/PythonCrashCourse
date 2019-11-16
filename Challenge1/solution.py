import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
from scipy.optimize import curve_fit


def expon(x,a,b,c):
        return a*np.exp(b*x)+c


data = pd.read_csv("challenge1.dat", header=None)
print(data)

t = data.iloc[:, 0].values
sig = data.iloc[:, 1].values
plt.figure()
plt.scatter(t, sig)

popt, pcov = curve_fit(expon, t, sig)

plt.figure()
t_new = np.linspace(0, 1, 100)
plt.scatter(t, sig, s=2)
plt.plot(t_new, expon(t_new, *popt), c='r', lw=4)
plt.show()

print("Optimised parameters: {}".format(popt))
print("Parameter error: {} ".format(np.sqrt(np.diag(pcov))))

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
from scipy.optimize import curve_fit

plt.rc('lines', linewidth=4)

def expon(x,a,b,c):
        return a*np.exp(b*x)+c


data = pd.read_csv("challenge1.dat", header=None)
print(data)

t = data.iloc[:, 0]
sig = data.iloc[:, 1]
plt.figure()
plt.scatter(t, sig)



popt, pcov = curve_fit(expon, t, sig)
plt.figure()
t_new = np.linspace(0, 1, 100)
plt.scatter(t, sig, s=2)
plt.plot(t_new, expon(t_new, *popt), c='r')

print("Optimised parameters: {}".format(popt))
print("Parameter error: {} ".format(np.sqrt(np.diag(pcov))))



# =============================================================================
# idx = np.random.randint(low=0, high=t.shape[0], size=1000)
# print(idx)
# t = t[idx]
# sig = sig[idx]
# plt.figure()
# plt.scatter(t, sig)
# =============================================================================


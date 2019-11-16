import matplotlib.pyplot as plt
import numpy as np
from scipy import stats, optimize

    # Polynomial fits

x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
plt.figure()
plt.scatter(x,y)
plt.show()


z = np.polyfit(x, y, deg=3)  #  coeff. with highest power first
print("\n p3 coeff.: {}".format(z))
p3 = np.poly1d(z)

z = np.polyfit(x, y, deg=30)
print("\n p30 coeff.: {}\n".format(z))
p30 = np.poly1d(z)

plt.figure()
xp = np.linspace(0, 5.5, 100)
plt.scatter(x,y,label='Original data')
plt.plot(xp, p3(xp), color='green',label='3rd degree')
plt.plot(xp, p30(xp), color='red', ls='--', label='30th degree')
plt.ylim([-2,2])
plt.title("Polynomial fits")
plt.legend()
plt.show()


    # Generic curve fitting

def f(x, a, b, c):
    return a*np.exp(-b*x)+c

#from scipy.optimize import *

x = np.linspace(0, 5, 50)
a = 5.0
b = 2.0
c = 0.5

plt.figure()
plt.scatter(x, f(x, a, b, c))
plt.title("Generic curve fitting - Original data")

# add some random noise
plt.figure()
y_noise = f(x, a, b, c) + 0.3*np.random.normal(size=len(x))
plt.scatter(x, y_noise)
plt.title("Generic curve fitting - Noisy data")
plt.show()


# fit data
guess = [3.0, 1.0, 1.0]
popt, pcov = optimize.curve_fit(f, x, y_noise, p0=guess, 
                       bounds=([1.0, 0.0, 0.0], [6., 3., 2.]))

print("\n Optimised parameters of the fit:\n {}".format(popt))
print("\n Covariance matrix of the parameters:\n {}".format(pcov))
perr = np.sqrt(np.diag(pcov))
print("\n One standard deviation errors on the parameters:\n {}".format(perr))


# calculate R squared: how much of the data is explained by the function used
residuals = y_noise - f(x, *popt)
ss_res = np.sum(residuals**2) # sum of the residuals squared: what the model does not explain
ss_tot = np.sum((y_noise-np.mean(y_noise))**2) # total sum of squares: proportional to data variance
Rsq = 1.0 - ss_res/ss_tot

plt.figure()
plt.scatter(x, y_noise)
strlabel = '$R^2 = $' + str(round(Rsq,4))
plt.plot(x, f(x, *popt), color='red', label=strlabel)
plt.title("Generic curve fitting - fitted data")
plt.legend()

    #  Gaussian Fit
    
def gauss(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

x = np.linspace(-5, 15, 200)
y = gauss(x, 1, 5, 2)
yn = y + 0.1 * np.random.normal(size=len(x))

plt.figure()
plt.plot(x,y)
plt.plot(x,yn)
plt.title("Gausssian noisy data")

popt, pcov = optimize.curve_fit(gauss, x, yn, p0=[5.0, 5.0, 1.0])
print("\n Optimised parameters of the fit:\n {}".format(popt))

plt.figure()
plt.plot(x, y, label='Original', color="red")
plt.scatter(x, yn, label='Original + Noise',s=10)
plt.plot(x, gauss(x, *popt), label='Fit', color="green")
plt.title("Gaussian Fit")
plt.legend()
#plt.show()


#    # Linear fit
#
#slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
#plt.figure()
#plt.scatter(x,y,label='Original data')
#xp = np.linspace(0, 5.5, 100)
#plt.plot(xp, slope*xp+intercept, color='green',label='linear fit')
#plt.ylim([-2,2])
#plt.legend()
#plt.title("Linear fit")
#plt.show()
#print("\n linear fit r-squared: {} \n".format(r_value**2))



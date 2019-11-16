import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

    # Numeric Differentiation 

def f(x, a, b, c, d):
    return a * np.sin(b*x + c) + d

a, b, c, d = 1.0, 4.0, 3.0, 1.0
dstep = 0.01
x = np.arange(-5, 5, dstep)
y = f(x, a, b, c, d)
plt.figure()
plt.plot(x, y, color='b')

plt.plot(x, np.gradient(y, dstep), color='r') #works for n-D functions, returns matrix
plt.title("Red is derivative of blue")
plt.show()

    # Numeric Integration 

x = np.linspace(0, 1, 10)
y = x
yn = x + 0.1*np.random.randn(len(x))
plt.figure()
plt.plot(x ,yn)
plt.scatter(x ,yn)
plt.title("Integrand function")
plt.show()

print("\nNumpy trapezoidal rule: {}".format(np.trapz(yn, x=x)))
print("SciPy trapezoidal rule: {}".format(integrate.trapz(yn, x=x)))
print("SciPy Simpson rule: {}".format(integrate.simps(yn, x=x)))

import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

    # 1D Interpolation

print("\n 1D Interpolation")
x = np.arange(0, 10)
y = np.exp(-x/3.0)
plt.scatter(x, y)
plt.show()

# 'kind' argument:
# string: ‘linear’, ‘nearest’, ‘zero’, ‘slinear’, ‘quadratic’, ‘cubic’
# where ‘zero’, ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline 
# interpolation of zeroth, first, second or third order
f = interpolate.interp1d(x, y, kind='quadratic')
xnew = np.arange(0, 9, 0.01)    
ynew = f(xnew)
plt.scatter(x,y, color='blue')
plt.plot(xnew,ynew, color='green', lw=2)
plt.show()


    # 2D Interpolation

print("\n 2D Interpolation")
def func(x, y):
    return (x+y)*np.exp(-2.0*(x**2 + y**2))

x, y = np.mgrid[-1:1:25j, -1:1:25j] # create 25 points including stop
fval = func(x, y)

from mpl_toolkits.mplot3d import Axes3D

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # nrows, ncols, and index
sf = ax.plot_surface(x, y, fval, cmap='jet')
fig.colorbar(sf)

# level plot
plt.figure()
plt.pcolormesh(x, y, fval, cmap='rainbow')

# interpolation
plt.figure()
f = interpolate.interp2d(x, y, fval, kind='cubic')
xn = np.arange(-1, 1, 0.01)
yn = np.arange(-1, 1, 0.01)
plt.pcolormesh(xn, yn, f(xn, yn), cmap='rainbow')


    # Data smoothing

#plt.rc("lines", lw=3, ls="-")
plt.figure()
x = np.arange(-5, 5, 0.1)
y = np.sin(x) + 0.25*np.random.rand(len(x))
plt.plot(x,y, lw=3, ls="-")

# Savitzky-Golay: https://en.wikipedia.org/wiki/Savitzky%E2%80%93Golay_filter#/media/File:Lissage_sg3_anim.gif

from scipy.signal import savgol_filter

ysg = savgol_filter(y, window_length=11, polyorder=2)
plt.figure()
plt.plot(x, y, label='Original', ls=":")
plt.plot(x, ysg, label='Savitzky-Golay', ls="-")
plt.legend()


    #   1D interpolation: Cubic spline
    
plt.figure()
x = np.arange(10)
y = np.sin(x)
plt.scatter(x,y, color="red")

cs = interpolate.CubicSpline(x, y)
xs = np.arange(-0.5, 9.6, 0.1)
 
plt.plot(xs, np.sin(xs), label='true', lw=5, ls="--")
plt.plot(xs, cs(xs), label="cubic spline", lw=2, ls="-")
plt.legend(loc='lower left')







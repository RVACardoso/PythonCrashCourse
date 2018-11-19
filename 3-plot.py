import numpy as np
import matplotlib.pyplot as plt
# %matplotlib auto
# %matplotlib inline
plt.rc('lines', linewidth=4)

    # Plot

x = np.arange(-5,5,0.1)
y = np.sin(x)
plt.plot(x,y,label='sin')
plt.title("Plot sin(x)")
plt.show()

    # Scatter

x = np.array([0,1,2,3,4,5,6])
y1 = np.array([6,5,4,3,2,1,0])
y2 = np.array([3,2,1,0,1,2,3])
plt.scatter(x, y1, label='Several labels!', c='r')
plt.plot(x, y2, label='Yes, you can add labels!')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.title("Scatter points")
plt.show()

    # Plot with fucntion

def func_plot(xdata, ydata): # should be on top of code
    plt.rc('lines', linewidth=8, linestyle='--')
    plt.rc('font', size=12)
    plt.plot(xdata, ydata, label="sin(x)", c='g')
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.title("A simple function")
    plt.show()
    
x = np.arange(0,5,0.1)
y = np.exp(x)
func_plot(xdata=x, ydata=y)



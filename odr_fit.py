from scipy import odr
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.linspace(0, 10, 50)
delta_x = 0.1
y = 2*x + 6 + 0.5*np.random.normal(size=len(x))
delta_y = 0.7*np.random.normal(size=len(x))

plt.scatter(x, y)
plt.show()


def f(B, x):
    return B[0]*x + B[1]

linear = odr.Model(f)
mydata = odr.Data(x, y, wd=1./delta_x, we=1./delta_y)

myodr = odr.ODR(data=mydata, model=linear, beta0=[3., 8.])

myoutput = myodr.run()
myoutput.pprint()


params = myoutput.beta
plt.plot(x, f(params, x), c='r')
plt.errorbar(x,y,delta_y,delta_x, '.')
plt.show()

chi2, p = stats.chisquare(y, f(params, x))
print("\n chi2: " + str(chi2))
print("\n chi2/(N-v): " + str(chi2/(len(y)-len(params))))

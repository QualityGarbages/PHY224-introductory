import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


data_1V = np.array([10.0, 15.0, 20.0, 25.0, 30.0, 35.0])
data_1A = np.array([0.80,1.2,1.6,2.,2.4,2.8])
Verr=np.array([0.03,0.03,0.03,0.03,0.04,0.04])
Aerr=np.array([0.01,0.01,0.01,0.01,0.01,0.01])

def fun(x, a):
    return a*x

popt, pconv = curve_fit(fun, data_1A, data_1V, sigma=Verr, absolute_sigma=True)

print(popt, pconv)

print("a is {:.4g} +- {:.4g}".format(popt[0], np.sqrt(pconv[0])[0]))

fig = plt.figure()
plt.errorbar(data_1A, data_1V, xerr=Aerr, yerr=Verr, fmt='o', ecolor = 'red', capsize=2, label='data')
plt.plot(data_1A, fun(data_1A, popt[0]), label="curve fit, V={:.4g}A".format(popt[0]))

plt.xlabel('Amps (A)', fontsize=10)
plt.ylabel('Voltage (V)', fontsize=10)


plt.xlim(0, 3)
plt.ylim(0, 40)
plt.legend()
plt.show()
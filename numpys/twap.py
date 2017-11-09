import numpy as np
c, v = np.loadtxt('data.csv', delimiter=',', usecols=(6, 7), unpack=True)
print(c, v)
t = np.arange(len(c))
twap = np.average(c, weights=t)
print(twap)
print(np.mean(c))

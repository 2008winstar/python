import numpy as np
c, v = np.loadtxt('data.csv', delimiter=',', usecols=(6, 7), unpack=True)
print(c, v)

print(np.average(3, weights=10))

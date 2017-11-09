import numpy as np


def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    return a + b


print(numpysum(10))

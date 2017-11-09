import numpy as np
import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt

x = np.arange(1, 5)
plt.plot(x, x * 1.5, x, x * 3.0, x, x/3.0)
# plt.show()
plt.savefig('test.png')

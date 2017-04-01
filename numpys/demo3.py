import numpy as np
A = np.matrix(
    [
        [3, 6, -5],
        [1, -3, 2],
        [5, -1, 4]
    ]
)
B = np.matrix(
    [
        [12],
        [-2],
        [10]
    ]
)
X = A ** (-1) * B
print(X)
print(A*X)

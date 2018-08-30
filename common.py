import numpy as np


def distence(v1, v2):
    v1[0] = abs(v1[0] - v2[0])
    v1[1] = abs(v1[1] - v2[1])
    return v1


v1 = np.array([1, 3])
v2 = np.array([2, 5])


a = np.linalg.norm(v1)
b = v1 / a
print(b)

import numpy as np


a = np.array([[1, -2, -2],
              [1, 0, -3],
              [1, -1, -2]])
print(a.shape)
t_value, t_xl = np.linalg.eig(a)
print(np.round(t_value, 1))
print(np.round(t_xl, 1))

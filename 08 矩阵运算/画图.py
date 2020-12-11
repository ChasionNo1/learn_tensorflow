import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['agg.path.chunksize'] = 40000

a = np.array([1.0]*20001)
b = np.array([0.0]*20001)
for i in range(20000):
    a[i+1] = a[i] + 3.1 * np.sin(a[i]) * np.sin([b[i]])
    b[i+1] = 2 * np.sin([a[i]]) + b[i]

# print(a)
# print(b)

plt.scatter(a, b)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('test.png', dpi=200)
plt.show()


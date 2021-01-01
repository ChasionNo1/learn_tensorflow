import numpy as np
import math
import matplotlib.pyplot as plt
# a = 19**2 + 25**2 + 31**2 + 38**2 + 44**2
# print(a)
# b = 19**4 + 25**4 + 31**4 + 38**4 + 44**4
# print(b)

x = np.linspace(0, 1, 500)
y = (x-1)**3
ax = plt.subplot(111)
plt.plot(y)
plt.show()

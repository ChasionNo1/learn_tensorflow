import numpy as np
import matplotlib.pyplot as plt

t1 = 1.5*np.arange(0, 1, 1/200)
t2 = np.arange(0, 0.05, 1/4000)

m = 2 + np.cos(10*np.pi*t1)
c = np.cos(200*np.pi*t2)


s = m * c
plt.figure(figsize=(10, 14))
ax = plt.subplot(311)
ax.set(ylim=[-2, 4])
ax.set_title('m')
plt.plot(t1, m)

ax = plt.subplot(312)
ax.set_title('c')
plt.plot(t2, c)

ax = plt.subplot(313)
ax.set_title('s')
plt.plot(t2, s)
plt.tight_layout(h_pad=5)
plt.show()

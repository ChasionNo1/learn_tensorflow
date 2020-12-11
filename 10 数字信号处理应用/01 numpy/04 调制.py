import numpy as np
import matplotlib.pyplot as plt

t_s = 0.000125
t_start = 0
t_end = 1
t = np.arange(t_start, t_end, 1.0/8000)
t2 = np.arange(t_start, t_end, 1.0/20000)

#  基带调制信号
# 直流分量
A0 = 2
m = np.cos(2000*np.pi*t) + np.cos(4000*np.pi*t)
m = m[:100]
# 载波
c = np.cos(10000*np.pi*t)
c = c[:100]

# 调幅
s = (A0 + m) * c

# 绘图
plt.figure(figsize=(10, 14))
ax = plt.subplot(411)
ax.set_title('m')
plt.plot(t[:100], m)

ax = plt.subplot(412)
ax.set_title('c')
plt.plot(t2[:100], c)

ax = plt.subplot(413)
ax.set_title('s')
plt.plot(s)
plt.tight_layout(h_pad=5)
plt.show()

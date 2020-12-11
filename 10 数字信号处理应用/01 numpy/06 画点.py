from scipy.fftpack import fft, fftshift, ifft
from scipy.fftpack import fftfreq
import numpy as np
import matplotlib.pyplot as plt


"""
t_s:采样周期
t_start:起始时间
t_end:结束时间


奈奎斯特采样定理：奈奎斯特抽样定理指若频带宽度有限的，要从抽样信号中无失真地恢复原信号，抽样频率应大于2倍信号最高频率。
"""
t_s = 0.0025
t_start = 0
t_end = 1
t = np.arange(t_start, t_end, t_s)

f0 = 5
f1 = 20

# 绘制图表
plt.figure(figsize=(13, 5))

# 构建原始信号序列  + np.random.randn(t.size)
y = 1.5*np.sin(2*np.pi*f0*t) + 3*np.sin(2*np.pi*f1*t)
ax = plt.subplot(211)
ax.set_title('Y1 original signal')
plt.plot(t, y)


# 采样点
ax = plt.subplot(212)
ax.set_title('sample point')
plt.scatter(t, y)
plt.show()

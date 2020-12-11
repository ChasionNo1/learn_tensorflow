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
t_s = 0.025
t_start = 0.5
t_end = 5
t = np.arange(t_start, t_end, t_s)

f0 = 5
f1 = 20

# 绘制图表
plt.figure(figsize=(10, 14))

# 构建原始信号序列  + np.random.randn(t.size)
y = 1.5*np.sin(2*np.pi*f0*t) + 3*np.sin(2*np.pi*f1*t)
ax = plt.subplot(411)
ax.set_title('Y1 original signal')
plt.plot(y)

'''
时域采样  + np.random.randn(sample_t.size)
'''
t_s_2 = 0.01
sample_t = np.arange(t_start, t_end, t_s_2)
ys = 1.5*np.sin(2*np.pi*f0*sample_t) + 3*np.sin(2*np.pi*20*sample_t)
ax = plt.subplot(412)

ax.set_title('Y2 Time Domain Sampling')
plt.plot(ys)

# plt.subplots_adjust(wspace =0, hspace =0)

'''
频域图
'''
Y = fft(y)
ax = plt.subplot(413)
ax.set_title('Y1 fft transform')
plt.plot(np.abs(Y))

Y1 = fft(ys)
ax = plt.subplot(414)
ax.set_title('Y2 fft transform')
plt.plot(np.abs(Y1))
plt.tight_layout(h_pad=5)


plt.show()

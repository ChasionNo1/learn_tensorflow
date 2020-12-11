from scipy.fftpack import fft, fftshift, ifft
from scipy.fftpack import fftfreq
import numpy as np
import matplotlib.pyplot as plt


"""
t_s:采样周期
t_start:起始时间
t_end:结束时间
"""
t_s = 0.01
t_start = 0.5
t_end = 5
t = np.arange(t_start, t_end, t_s)

f0 = 5
f1 = 20

# 绘制图表
plt.figure(figsize=(10, 12))

# 构建原始信号序列
y = 1.5*np.sin(2*np.pi*f0*t) + 3*np.sin(2*np.pi*20*t) + np.random.randn(t.size)
ax=plt.subplot(511)
ax.set_title('original signal')
plt.tight_layout()
plt.plot(y)

"""
FFT(Fast Fourier Transformation)快速傅里叶变换
"""
Y = fft(y)
ax=plt.subplot(512)
ax.set_title('fft transform')
plt.plot(np.abs(Y))

"""
Y = fftshift(X) 通过将零频分量移动到数组中心，重新排列傅里叶变换 X。
"""
shift_Y = fftshift(Y)
ax=plt.subplot(513)
ax.set_title('shift fft transform')
plt.plot(np.abs(shift_Y))

"""
得到正频率部分
"""
pos_Y_from_fft = Y[:Y.size//2]
ax=plt.subplot(514)
ax.set_title('fft transform')
plt.tight_layout()
plt.plot(np.abs(pos_Y_from_fft))

"""
直接截取 shift fft结果的前半部分
"""
pos_Y_from_shift = shift_Y[shift_Y.size//2:]
ax=plt.subplot(515)
ax.set_title('shift fft cut')
plt.plot(np.abs(pos_Y_from_shift))
plt.show()
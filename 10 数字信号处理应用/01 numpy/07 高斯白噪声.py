"""
加性高斯白噪声：白是指功率谱恒定，概率px满足高斯分布
在通信中指的是一种各频谱分量服从均匀分布，且幅度服从高斯分布的噪声信号
功率谱密度：G(w)=N0/2, N0是正实常数。

SNR=10*log((sigmax2)/(sigman2)),x为原始信号，n为噪声信号，sigma求和
得到噪声信号的表达式为：
n = sigma(x2)/N*10^(SNR/10), N是原始信号的长度
最后服从高斯分布对噪声信号进行放大，可以得到最终的噪声信号：
noise = random(N)*sqrt(abs(n))
"""
import numpy as np
import matplotlib.pyplot as plt


def awgn(x, snr, seed=3):
    """
    加性高斯白噪声
    :param x: 原始信号
    :param snr: 信噪比, 10lg(Ps/Pn),Ps和Pn分别代表信号和噪声的有效功率,信噪比的计量单位是dB
    :param seed:
    :return:
    """
    np.random.seed(seed)
    snr = 10**(snr/10)
    xpower = np.sum(x**2)/len(x)
    npower = xpower/snr
    noise = np.random.randn(len(x)) * np.sqrt(npower)
    return x + noise


# 构建原始信号序列  + np.random.randn(t.size)
t_s = 0.0025
t_start = 0
t_end = 1
t = np.arange(t_start, t_end, t_s)

f0 = 5
f1 = 20
# 原始信号
y = 1.5*np.sin(2*np.pi*f0*t) + 3*np.sin(2*np.pi*f1*t)
plt.figure(figsize=(13, 5))
ax = plt.subplot(311)
ax.set_title('y,f1=5,f2=20')
plt.plot(y)
# 加入噪声后
ax = plt.subplot(312)
ax.set_title('yn,10db')
yn = awgn(y, 10)
plt.plot(yn)


# 单独噪声信号
n = 400
while_noise = np.random.standard_normal(size=n)
ax = plt.subplot(313)
ax.set_title('white_noise')
plt.plot(while_noise)

plt.tight_layout(h_pad=5)
plt.show()


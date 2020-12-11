import thinkdsp
import matplotlib.pyplot as plt

con_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
con_sig.plot()
wave = con_sig.make_wave(duration=0.5, start=0, framerate=11025)
spectrum = wave.make_spectrum()
spectrum.plot()
plt.show()

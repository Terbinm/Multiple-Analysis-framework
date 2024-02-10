import numpy as np
import matplotlib.pyplot as plt

# 建立時間軸
t = np.linspace(0, 0.5, 500)

# 建立一個包含兩種頻率的信號
# s = np.sin(40 * 2 * np.pi * t) + 0.5 * np.sin(90 * 2 * np.pi * t)
s = np.sin(40 * 2 * np.pi * t)

# 進行傅立葉變換
fft = np.fft.fft(s)

# 計算頻率軸
T = t[1] - t[0]  # 採樣間隔
N = s.size
f = np.linspace(0, 1 / T, N)

# 繪製原始信號
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.title('Original signal')

# 繪製傅立葉變換結果
plt.subplot(2, 1, 2)
plt.plot(f[:N // 2], np.abs(fft)[:N // 2] * 1 / N)  # 乘以 1/N 進行歸一化
plt.title('Fourier Transform')
plt.show()

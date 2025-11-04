import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# === Parameters ===
fs = 48000           # Sampling rate (Hz)
fc = 1000            # Cutoff frequency (Hz)
G  = 6               # Gain in dB
H0 = 10**(G/20) - 1  # shelving gain factor
LF = True            # True -> Low-shelf, False -> High-shelf

# === Derived values ===
theta_c = 2 * np.pi * fc / fs
aB = (np.sin(theta_c) - np.cos(theta_c)) / (np.sin(theta_c) + np.cos(theta_c))
C  = np.sqrt(H0 + 1) if LF else 1 / np.sqrt(H0 + 1)

# === First-order allpass ===
# A(z) = (z^-1 + aB/C) / (1 + aB/C * z^-1)
b_ap = np.array([1, aB/C])
a_ap = np.array([aB/C, 1])

# === Shelving filter ===
# H(z) = 1 + H0/2 * [1 ± A(z)]
# '+' for low-shelf, '-' for high-shelf
sign = +1 if LF else -1
b_shelf = signal.convolve([1], b_ap) * (H0/2 * sign) + [1 + H0/2]
a_shelf = a_ap

# === Frequency response ===
w, h = signal.freqz(b_shelf, a_shelf, worN=1024)
freq = w * fs / (2 * np.pi)

plt.figure(figsize=(8, 4))
plt.plot(freq, 20 * np.log10(abs(h)), label='Shelving Filter')
plt.title(f'{"Low" if LF else "High"}-Shelf Filter (Gain = {G} dB)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parâmetros
M = 20
i = np.arange(M)

# Janelas
hamming = 0.54 - 0.46 * np.cos(2 * np.pi * i / (M - 1))
blackman = 0.42 - 0.5 * np.cos(2 * np.pi * i / (M - 1)) + 0.08 * np.cos(4 * np.pi * i / (M - 1))

# Calcula resposta em frequência H(e^{jω}) com freqz
w_h, H_h = signal.freqz(hamming, worN=4096)    # w em rad/sample
w_b, H_b = signal.freqz(blackman, worN=4096)

# Converte para frequência normalizada (cycles/sample), onde 0.5 = Nyquist
f_h = w_h / (2 * np.pi)
f_b = w_b / (2 * np.pi)

# Magnitude normalizada (dB)
Hh_db = 20 * np.log10(np.abs(H_h) / np.max(np.abs(H_h)))
Hb_db = 20 * np.log10(np.abs(H_b) / np.max(np.abs(H_b)))

# Plot magnitude (dB) - janela inteira 0..0.5
plt.figure(figsize=(10,5))
plt.plot(f_h, Hh_db, label='Hamming')
plt.plot(f_b, Hb_db, label='Blackman')
plt.xlim(0, 0.5)
plt.ylim(-120, 5)
plt.xlabel('Frequência normalizada (cycles/sample)')
plt.ylabel('Magnitude (dB), normalizada @ 0 dB')
plt.title('Resposta em frequência (magnitude) - Hamming vs Blackman')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot magnitude linear (zoom na banda passante)
plt.figure(figsize=(10,4))
plt.plot(f_h, np.abs(H_h)/np.max(np.abs(H_h)), label='Hamming')
plt.plot(f_b, np.abs(H_b)/np.max(np.abs(H_b)), label='Blackman')
plt.xlim(0, 0.2)
plt.xlabel('Frequência normalizada (cycles/sample)')
plt.ylabel('Magnitude, normalizada @ 1')
plt.title('Resposta em frequência (magnitude linear) - Zoom na banda passante')
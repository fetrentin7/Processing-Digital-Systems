import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parâmetros
M = 20
i = np.arange(M)
fc_hz = 400
fs = 8000
fc = fc_hz / fs  # frequência de corte normalizada

# Filtro ideal (sinc) - cálculo manual
sinc = np.zeros(M)
for n in range(M):
    x = n - (M - 1) / 2
    if x == 0:
        sinc[n] = 2 * fc
    else:
        sinc[n] = 2 * fc * np.sin(2 * np.pi * fc * x) / (2 * np.pi * fc * x)

# Resposta em frequência
w, H = signal.freqz(sinc, worN=1024)

# Plot magnitude (dB)
plt.figure(figsize=(10,5))
plt.plot(w / (2*np.pi), label='Sinc ideal')

plt.xlim(-0.06, 0.5)  # intervalo ajustado conforme solicitado
plt.ylim(-120, 5)
plt.xlabel('Frequência normalizada (cycles/sample)')
plt.ylabel('Magnitude (dB), normalizada @ 0 dB')
plt.title('Resposta em frequência - Filtro Sinc ideal (fc = 0.05)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
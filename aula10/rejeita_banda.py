import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# --- Parâmetros ---
F1 = 0.10   # Frequência de corte inferior (0 a 0.5)
F2 = 0.25   # Frequência de corte superior (0 a 0.5)
M = 100     # Comprimento do filtro (resulta em N = 101 coeficientes)
N = M + 1

# --- Função auxiliar: filtro passa-baixas ---
def fir_lowpass(fc, M):
    N = M + 1
    h = np.zeros(N)
    for i in range(N):
        x = i - M / 2
        if x == 0:
            h[i] = 2 * np.pi * fc
        else:
            h[i] = np.sin(2 * np.pi * fc * x) / x
        # Aplica janela de Hamming
        h[i] *= (0.54 - 0.46 * np.cos(2 * np.pi * i / M))
    # Normaliza para ganho unitário em DC
    h /= np.sum(h)
    return h

# --- Filtros passa-baixas nas duas frequências ---
h_lp1 = fir_lowpass(F1, M)
h_lp2 = fir_lowpass(F2, M)

# --- Passa-banda é a diferença ---
h_bp = h_lp2 - h_lp1

# --- Resposta em frequência ---
w, H = signal.freqz(h_bp, worN=1024)
freq_norm = w / (2 * np.pi)

# --- Plot da resposta em frequência ---
plt.figure(figsize=(10, 5))
plt.plot(freq_norm, 20 * np.log10(np.abs(H) / np.max(np.abs(H))))
plt.axvline(F1, color='r', linestyle='--', label=f'F1 = {F1}')
plt.axvline(F2, color='r', linestyle='--', label=f'F2 = {F2}')
plt.title('Resposta em Frequência - Filtro Passa-Banda (Janela de Hamming)')
plt.xlabel('Frequência Normalizada (ciclos/amostra)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

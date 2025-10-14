import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
PI = 3.14159265
FC = 0.14  # frequência de corte (entre 0 e 0.5)
M = 100    # comprimento do filtro (101 pontos)
N = M + 1  # número de coeficientes

# Inicializa o vetor do filtro
h = np.zeros(N)

for i in range(N):
    x = i - M / 2
    if x == 0:
        h[i] = 2 * PI * FC
    else:
        h[i] = np.sin(2 * PI * FC * x) / x
    # Aplica janela de Hamming
    h[i] *= (0.54 - 0.46 * np.cos(2 * PI * i / M))

# Normaliza para ganho unitário em DC
soma = np.sum(h)
h = h / soma

w, H = signal.freqz(h, worN=1024)
frequencia_normalizada = w / (2 * np.pi)

n_amostras = 200
n = np.arange(n_amostras)
frequencia_sinal = 0.05  # frequência normalizada do sinal de entrada
x = np.sin(2 * np.pi * frequencia_sinal * n)

# Saída do filtro FIR: y[n] = h0*x[n] + h1*x[n-1] + ... + hM*x[n-M]
y = np.convolve(x, h, mode='full')[:n_amostras]

plt.figure(figsize=(10, 5))
plt.plot(n, x, label='Entrada x[n]')
plt.plot(n, y, label='Saída y[n]')
plt.title('Resposta do Filtro FIR à Entrada x[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


idx_fc = np.argmin(np.abs(frequencia_normalizada - FC))
print(f"Resposta em frequência na frequência de corte (FC={FC}): {20*np.log10(np.abs(H[idx_fc]) / np.max(np.abs(H))):.2f} dB")

# ...existing code...

# Salva o vetor h em um arquivo txt
np.savetxt("coeficientes_filtro.txt", h, fmt="%.10f")
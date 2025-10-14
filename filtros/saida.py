import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

FC = 0.14  # frequência de corte (entre 0 e 0.5)
M = 100    # comprimento do filtro (101 pontos)
N = M + 1  # número de coeficientes

# Inicializa o vetor do filtro
h = np.zeros(N)

for i in range(N):
    x = i - M / 2
    if x == 0:
        h[i] = 2 * np.pi * FC
    else:
        h[i] = np.sin(2 * np.pi * FC * x) / x
    # Aplica janela de Hamming
    h[i] *= (0.54 - 0.46 * np.cos(2 * np.pi * i / M))

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

# ...existing code...

# Plot da resposta em frequência do filtro (amplitude linear)
plt.figure(figsize=(10, 5))
plt.plot(frequencia_normalizada, np.abs(H) / np.max(np.abs(H)))
plt.axvline(FC, color='r', linestyle='--', label=f'Frequência de corte (FC={FC})')
plt.title('Resposta em Frequência do Filtro Passa-Baixas (Amplitude Linear)')
plt.xlabel('Frequência Normalizada (ciclos/amostra)')
plt.ylabel('Amplitude Normalizada')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
idx_fc = np.argmin(np.abs(frequencia_normalizada - FC))
print(f"Resposta em frequência na frequência de corte (FC={FC}): {20*np.log10(np.abs(H[idx_fc]) / np.max(np.abs(H))):.2f} dB")

# ...existing code...

# Salva o vetor h em um arquivo txt
np.savetxt("coeficientes_filtro.txt", h, fmt="%.10f")
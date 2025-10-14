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

# Exemplo de plot do kernel do filtro
plt.stem(np.arange(N), h)
plt.title('Coeficientes do Filtro Passa-Baixas (Janela de Hamming)')
plt.xlabel('Amostra')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 5))
plt.plot(frequencia_normalizada, 20 * np.log10(np.abs(H) / np.max(np.abs(H))))
plt.title('Resposta em Frequência do Filtro Passa-Baixas')
plt.xlabel('Frequência Normalizada (ciclos/amostra)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.tight_layout()
plt.show()

idx_fc = np.argmin(np.abs(frequencia_normalizada - FC))
print(f"Resposta em frequência na frequência de corte (FC={FC}): {20*np.log10(np.abs(H[idx_fc]) / np.max(np.abs(H))):.2f} dB")
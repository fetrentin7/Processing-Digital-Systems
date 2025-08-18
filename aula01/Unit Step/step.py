import numpy as np
import matplotlib.pyplot as plt
import os

# Parâmetros do sinal
fs = 8000  # Frequência de amostragem
duracao = 1  # Duração total da simulação em segundos
amplitude = 16384  # Amplitude do sinal

# --- Geração do Sinal de Impulso Unitário Discreto ---

# Sinal discreto
ts = 1 / fs  # Período de amostragem
n = np.arange(0, int(duracao * fs))

# 1. Começa com um sinal discreto de zeros
xd = np.zeros_like(n, dtype=float) # Usar float para a atribuição da amplitude

# 2. Define a amplitude APENAS na primeira amostra (n=0)
xd[0] = amplitude


# --- Plotagem ---
plt.figure(figsize=(10, 8))

# Gráfico 1: Impulso no domínio do tempo (segundos)
plt.subplot(2, 1, 1)
plt.stem(n * ts, xd, 'r', basefmt=" ", linefmt='r-', markerfmt='ro')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.title(f'Impulso Unitário Discreto (no tempo)')
plt.grid(True)
plt.ylim([-1000, amplitude + 1000])

# Gráfico 2: Impulso no domínio das amostras
plt.subplot(2, 1, 2)
plt.stem(n, xd)
plt.title('Impulso Unitário Discreto (em amostras)')
plt.xlabel('Amostras [n]')
plt.ylabel('x[n]')
plt.grid(True)
plt.xlim([-10, 50]) # Zoom no eixo X para ver melhor o impulso no início
plt.ylim([-1000, amplitude + 1000])

plt.tight_layout()
plt.show()

# --- Salvando o arquivo .pcm ---

# Converter o sinal para inteiros de 16 bits
sinal_int16 = xd.astype(np.int16)

# Definir o nome do arquivo
nome_arquivo = 'impulso_unitario.pcm'

# Salvar o arquivo .pcm
with open(nome_arquivo, 'wb') as f:
    f.write(sinal_int16.tobytes())

print(f'Sinal salvo como "{nome_arquivo}"')
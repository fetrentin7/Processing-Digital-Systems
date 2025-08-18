import numpy as np
import matplotlib.pyplot as plt
import os

# Parâmetros do sinal
fs = 8000  # Frequência de amostragem
duracao = 3  # Duração em segundos (3s para ver bem o decaimento)
amplitude = 16384  # Amplitude inicial do sinal

# Parâmetro da exponencial
alpha = 1.5  # Constante de decaimento. Aumente para um decaimento mais rápido.

# --- Geração do Sinal Exponencial Decrescente ---

# Sinal "analógico" (simulado com alta resolução para visualização)
dt = 1 / (fs * 10)
t = np.arange(0, duracao, dt)
xa = amplitude * np.exp(-alpha * t)


# Sinal discreto
ts = 1 / fs  # Período de amostragem
n = np.arange(0, int(duracao * fs))
xd = amplitude * np.exp(-alpha * n * ts)


# --- Plotagem ---
plt.figure(figsize=(10, 8))

# Gráfico 1: Sinal "analógico" e amostrado no domínio do tempo (segundos)
plt.subplot(2, 1, 1)
plt.plot(t, xa, label='Sinal Original (Exponencial)')
plt.stem(n * ts, xd, 'r', basefmt=" ", linefmt='r-', markerfmt='ro', label='Sinal Amostrado')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.title(f'Sinal Exponencial Decrescente (alpha={alpha})')
plt.grid(True)
plt.legend()


# Gráfico 2: Sinal amostrado no domínio das amostras
plt.subplot(2, 1, 2)
plt.stem(n, xd)
plt.title('Sinal Amostrado (Exponencial Decrescente)')
plt.xlabel('Amostras [n]')
plt.ylabel('x[n]')
plt.grid(True)

plt.tight_layout()
plt.show()

# --- Salvando o arquivo .pcm ---

# Converter o sinal para inteiros de 16 bits
sinal_int16 = xd.astype(np.int16)

# Definir o nome do arquivo
nome_arquivo = 'exponencial_decrescente.pcm'

# Salvar o arquivo .pcm
with open(nome_arquivo, 'wb') as f:
    f.write(sinal_int16.tobytes())

print(f'Sinal salvo como "{nome_arquivo}"')
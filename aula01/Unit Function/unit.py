import numpy as np
import matplotlib.pyplot as plt
import os

# Parâmetros do sinal
fs = 10  # Frequência de amostragem
duracao = 2  # Duração total da simulação em segundos (para ver o pulso terminar)
amplitude = 16384  # Amplitude do sinal

# --- Geração do Sinal de Pulso Retangular ---

# Sinal "analógico" (simulado com alta resolução para visualização)
dt = 1 / (fs * 10)
t = np.arange(0, duracao, dt)

# 1. Começa com um sinal de zeros
xa = np.zeros_like(t)
# 2. Define a amplitude apenas para o intervalo onde t <= 1
xa[t <= 1] = amplitude


# Sinal discreto
ts = 1 / fs  # Período de amostragem
n = np.arange(0, int(duracao * fs))

# 1. Começa com um sinal discreto de zeros
xd = np.zeros_like(n)
# 2. Define a amplitude para as amostras que correspondem a t <= 1
#    Um segundo de duração corresponde a 'fs' amostras.
numero_de_amostras_do_pulso = int(fs * 1)
xd[:numero_de_amostras_do_pulso] = amplitude


# --- Plotagem ---
plt.figure(figsize=(10, 8))

# Gráfico 1: Sinal "analógico" e amostrado no domínio do tempo (segundos)
plt.subplot(2, 1, 1)
plt.plot(t, xa, label='Sinal Original (Pulso)')
plt.stem(n * ts, xd, 'r', basefmt=" ", linefmt='r-', markerfmt='ro', label='Sinal Amostrado')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.title(f'Sinal de Pulso Retangular ({duracao}s)')
plt.grid(True)
plt.legend()
plt.ylim([-1000, amplitude + 1000]) # Ajusta o limite do eixo Y para ver o zero

# Gráfico 2: Sinal amostrado no domínio das amostras
plt.subplot(2, 1, 2)
plt.stem(n, xd)
plt.title('Sinal Amostrado (Pulso Retangular)')
plt.xlabel('Amostras [n]')
plt.ylabel('x[n]')
plt.grid(True)
plt.ylim([-1000, amplitude + 1000]) # Ajusta o limite do eixo Y

plt.tight_layout()
plt.show()

# --- Salvando o arquivo .pcm ---

# Converter o sinal para inteiros de 16 bits
sinal_int16 = xd.astype(np.int16)

# Definir o nome do arquivo
nome_arquivo = 'pulso_retangular.pcm'

# Salvar o arquivo .pcm
with open(nome_arquivo, 'wb') as f:
    f.write(sinal_int16.tobytes())

print(f'Sinal salvo como "{nome_arquivo}"')
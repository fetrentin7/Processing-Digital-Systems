import numpy as np
import matplotlib.pyplot as plt
import os

fs = 8000

f1 = 200
duracao = 1
amplitude = 16384 # Define a amplitude do sinal para 16384 (máximo para int16)
A1 = (amplitude * 0.5)

f2 = 1000
duracao = 1
amplitude = 16384 # Define a amplitude do sinal para 16384 (máximo para int16)
A2 = (amplitude * 0.3)


# Sinal analógico (simulado com alta resolução)
dt = 1 / (fs * 10) # Intervalo de tempo para simulação de alta resolução
t = np.arange(0, duracao, dt) # Gerar sinal por 1 segundo
xa1 = A1 * np.cos(2 * np.pi * f1 * t)
xa2 = A2 * np.cos(2 * np.pi * f2 * t)
xa = xa1 + xa2

# Sinal discreto
ts = 1 / fs # Período de amostragem
n = np.arange(0, int(duracao * fs)) # Gerar amostras para 1 segundo
# Sample the continuous signal at the discrete time points
xd = A1 * np.cos(2 * np.pi * f1 * n * ts) + A2 * np.cos(2 * np.pi * f2 * n * ts)
# Scale to the desired amplitude and convert to integer
xd = (xd * (amplitude / max(abs(xd)))).astype(np.int16)


# Plota o sinal analógico
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.plot(t, xa) # Plotar em segundos
plt.xlabel('Tempo [s]')
plt.ylabel('xa(t)')
plt.title(f'Sinal de Freq = {f1}Hz e {f2}Hz ({duracao}s)')
plt.grid(True)

# Sinal discreto
# Plota o sinal discreto no mesmo gráfico do sinal analógico
plt.stem(n * ts, xd, 'r', label='Sinal Amostrado') # Plotar em segundos
plt.legend()


# Plota o sinal amostrado em um gráfico separado
plt.subplot(2, 1, 2)
plt.stem(n, xd)
plt.title('Sinal Amostrado')
plt.xlabel('Amostras')
plt.ylabel('x[n]')
plt.grid(True)

plt.tight_layout()
plt.show()

# Salvar o sinal discreto como arquivo .pcm
# Converter o sinal para inteiros de 16 bits
sinal_int16 = xd.astype(np.int16)

# Definir o nome do arquivo
nome_arquivo = 'sinal_senoidal_somado.pcm'

# Salvar o arquivo .pcm
with open(nome_arquivo, 'wb') as f:
    f.write(sinal_int16.tobytes())

print(f'Sinal salvo como "{nome_arquivo}"')
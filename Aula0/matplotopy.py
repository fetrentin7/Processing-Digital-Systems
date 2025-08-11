import numpy as np
import matplotlib.pyplot as plt

# Lendo arquivo binário (16 bits assinados)
with open('Sweep.pcm', 'rb') as f:
    s = np.fromfile(f, dtype=np.int16)

itera = len(s)

# Plot do sinal de entrada
plt.subplot(2, 1, 1)
plt.plot(s)
plt.grid(True)
plt.title('Sinal de entrada')

# Salvar valores intermediários
sav_y = np.zeros(itera, dtype=np.int16)

ganho = 2

for j in range(itera):
    x = s[j] #Amostra sinal entrada
    y = ganho * x
    # Garantir que o valor continua dentro do intervalo int16
    if y > 32767:
        y = 32767
    elif y < -32768:
        y = -32768
    sav_y[j] = y

# Plot da saída
plt.subplot(2, 1, 2)
plt.plot(sav_y, 'r')
plt.title('Saída')
plt.xlabel('Número de amostras')
plt.ylabel('Amplitude da saída')
plt.grid(True)
plt.tight_layout()
plt.show()

# Salvando o arquivo de saída
with open('sinal_saida.pcm', 'wb') as f:
    sav_y.tofile(f)

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# 1. Especificações do filtro (do quadro)
fc = 400  
fs = 8000 
ordem = 1 

# 2. Projetar o filtro e obter os coeficientes (b, a)
#    A função 'butter' é um tipo de filtro IIR muito comum e estável.
#    Ela calcula os coeficientes para você.
b, a = signal.butter(ordem, fc, btype='low', fs=fs)

print(f"Coeficientes do Filtro (Numerador): b = {b}")
print(f"Coeficientes do Filtro (Denominador): a = {a}")
print("\nPerceba como o segundo valor do coeficiente 'a' é próximo do seu cálculo de 'b' no quadro!")

# 3. Criar um sinal de teste para filtrar
#    Sinal composto por uma onda de 100 Hz e uma de 1500 Hz
duracao = 1.0  # 1 segundo de sinal
t = np.linspace(0, duracao, int(fs * duracao), endpoint=False)
sinal_entrada = 0.7 * np.sin(2 * np.pi * 100 * t) + 0.3 * np.sin(2 * np.pi * 1500 * t)

# 4. Aplicar o filtro ao sinal de entrada
sinal_filtrado = signal.lfilter(b, a, sinal_entrada)

# 5. Visualizar os resultados
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, sinal_entrada)
plt.title("Sinal Original (100 Hz + 1500 Hz)")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.xlim(0, 0.05) 

plt.subplot(2, 1, 2)
plt.plot(t, sinal_filtrado)
plt.title("Sinal Filtrado (Passa-Baixas em 400 Hz)")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.xlim(0, 0.05)

plt.tight_layout()
plt.show()
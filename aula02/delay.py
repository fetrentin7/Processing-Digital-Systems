import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
Fs = 8000
t1 = 1.0e-3
t2 = 1.5e-3
delay = 0.15
# Exemplo de delay
n1 = int(delay * Fs)
n2 = int(delay * Fs)

# Ganhos
a0 = 0.5
a1 = 0.3
a2 = 0.2

# Vetor de delay
tama_delay = n2
vetor_delay = np.zeros(tama_delay)

# Entrada (impulso unitário)
entrada = np.zeros(2 * tama_delay)
entrada[0] = 1  # impulso unitário

# Saída
tama_loop = len(entrada)
vet_saida = np.zeros(tama_loop)

# Loop principal
for j in range(tama_loop):
    input_val = entrada[j]
    vetor_delay[0] = input_val
    
    y = a0 * vetor_delay[0] \
        + a1 * (vetor_delay[n1 - 1] if n1 < tama_delay else 0) \
        + a2 * (vetor_delay[n2 - 1] if n2 <= tama_delay else 0)
    
    # Desloca o vetor de delay (shift)
    vetor_delay[1:] = vetor_delay[:-1]
    
    vet_saida[j] = y

# Plot
plt.stem(vet_saida)
plt.title("Resposta ao Impulso com Delay")
plt.xlabel("Amostras")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --- Definição do Sistema ---
# A equação de diferenças é: y[n] - 0.95y[n-1] = x[n] - x[n-1]
# A função de transferência correspondente é H(z) = (1 - z^-1) / (1 - 0.95z^-1)

# Coeficientes do numerador (polinômio em z^-1 associado a x[n])
b = [1, -1]

# Coeficientes do denominador (polinômio em z^-1 associado a y[n])
a = [1, -0.95]

# Define o sistema LTI 
# O terceiro argumento '1' representa o tempo de amostragem dt=1.
system = (b, a, 1)

# --- Cálculo das Respostas ---

# Define o número de amostras 
n_samples = 30

# a) Cálculo da Resposta ao Impulso
# A função dimpulse calcula a saída h[n] quando a entrada é um impulso unitário.
t_impulse, h = signal.dimpulse(system, n=n_samples)

# A saída de 'dimpulse' é um array 2D,  squeeze para converter para 1D.
h = np.squeeze(h)

# b) Cálculo da Resposta ao Degrau
# A função dstep calcula a saída s[n] quando a entrada é um degrau unitário.
t_step, s = signal.dstep(system, n=n_samples)

# Converte a saída para um array 1D para facilitar a plotagem.
s = np.squeeze(s)


# --- d) Plotagem dos Gráficos ---

# Cria uma figura para conter os dois gráficos, com um tamanho total de 14x6 polegadas.
plt.figure(figsize=(14, 6))

# Gráfico 1: Resposta ao Impulso
plt.subplot(1, 2, 1) # (1 linha, 2 colunas, 1º gráfico)

plt.stem(t_impulse, h)
plt.title('a) Resposta ao Impulso $h[n]$')
plt.xlabel('Amostra (n)')
plt.ylabel('Amplitude')
plt.grid(True) # Adiciona uma grade para melhor visualização

# Gráfico 2: Resposta ao Degrau
plt.subplot(1, 2, 2) # (1 linha, 2 colunas, 2º gráfico)

plt.stem(t_step, s)
plt.title('b) Resposta ao Degrau $s[n]$')
plt.xlabel('Amostra (n)')
plt.ylabel('Amplitude')
plt.grid(True)

# Ajusta o espaçamento entre os gráficos para que não se sobreponham.
plt.tight_layout()

# Exibe a janela com os gráficos gerados.
plt.show()
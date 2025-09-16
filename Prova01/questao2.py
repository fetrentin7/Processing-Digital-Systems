import numpy as np
import matplotlib.pyplot as plt


# Define o intervalo de tempo para o cálculo e plotagem (n de 0 a 8)
n = np.arange(9)

# Define a entrada x[n] = u[n] - u[n-2]
# Isso resulta em um sinal que é 1 em n=0 e n=1, e 0 nos outros pontos.
x = np.zeros_like(n, dtype=float)
x[0] = 1
x[1] = 1

# Define a resposta ao impulso h[n] = (0.5)^n * u[n]
h = (0.5)**n

# --- 2. Cálculo da Convolução ---

# Calcula a convolução y[n] = x[n] * h[n] 
y_completo = np.convolve(x, h)

# O resultado da convolução é mais longo. Pegamos apenas os valores
# correspondentes ao nosso intervalo de interesse (n de 0 a 8).
y = y_completo[:9]


# --- 3. Geração e Plotagem do Gráfico ---

print("Gerando o gráfico...")

# Cria a janela do gráfico com um tamanho específico
plt.figure(figsize=(12, 6))

# --- Gráfico da Esquerda: Saída da Convolução y[n] ---
plt.subplot(1, 2, 1) # Cria o primeiro subplot (1 linha, 2 colunas, posição 1)
plt.stem(n, y)
plt.title("a) Saída da Convolução $y[n] = x[n] * h[n]$")
plt.xlabel("Amostra (n)")
plt.ylabel("Amplitude y[n]")
plt.xticks(n) # Mostra todos os números no eixo n
plt.grid(True) # Adiciona uma grade de fundo

# --- Gráfico da Direita: Resposta ao Impulso h[n] ---
plt.subplot(1, 2, 2) # Cria o segundo subplot (1 linha, 2 colunas, posição 2)
plt.stem(n, h)
plt.title("b) Resposta ao Impulso $h[n] = (0.5)^n u[n]$")
plt.xlabel("Amostra (n)")
plt.ylabel("Amplitude h[n]")
plt.xticks(n)
plt.grid(True)

# Ajusta o layout para que os títulos e eixos não se sobreponham
plt.tight_layout()

# Exibe a janela com os gráficos
plt.show()

print("Gráfico exibido.")
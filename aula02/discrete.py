import numpy as np
import matplotlib.pyplot as plt
import os

# Parâmetros do sinal
fs = 100  # Frequência de amostragem
duracao = 1   # Duração total da simulação em segundos
amplitude = 1500   # Amplitude do sinal

# --- Geração do Sinal de Impulso Unitário Discreto ---

# Sinal discreto
ts = 1 / fs   # Período de amostragem
n = np.arange(0, int(duracao * fs))

# 1. Começa com um sinal discreto de zeros
xd = np.zeros_like(n, dtype=float) # Usar float para a atribuição da amplitude

# 2. Define a amplitude APENAS na primeira amostra (n=0)
xd[0] = amplitude

# --- Aplicação do Bloco de Diferença com Modificação ---
# Para que o cálculo funcione como um filtro (usando a entrada original),
# primeiro criamos uma cópia do sinal de impulso.
xd_original = np.copy(xd)

# O bloco de processamento é mantido, conforme solicitado.
for i in range(1, len(xd)):
    # 1. O bloco calcula a diferença original
    valor_calculado = xd_original[i] - xd_original[i-1]
    
    # 2. Adicionamos uma regra: se o valor for negativo, ele vira 0.
    #    Isso impede o aparecimento do impulso negativo no resultado final.
    if valor_calculado < 0:
        xd[i] = 0
    else:
        xd[i] = valor_calculado


# --- Plotagem ---
plt.figure(figsize=(10, 8))

# Gráfico 1: Sinal resultante no domínio do tempo (segundos)
plt.subplot(2, 1, 1)
plt.stem(n * ts, xd, 'r', basefmt=" ", linefmt='r-', markerfmt='ro')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.title(f'Sinal Processado pelo Bloco Modificado (no tempo)')
plt.grid(True)
# Ajusta o limite do eixo Y para uma melhor visualização
plt.ylim([-1000, amplitude + 1000])

# Gráfico 2: Sinal resultante no domínio das amostras
plt.subplot(2, 1, 2)
plt.stem(n, xd)
plt.title('Sinal Processado pelo Bloco Modificado (em amostras)')
plt.xlabel('Amostras [n]')
plt.ylabel('x[n]')
plt.grid(True)
plt.xlim([-10, 50]) # Zoom no eixo X para ver melhor o impulso no início
# Ajusta o limite do eixo Y para uma melhor visualização
plt.ylim([-1000, amplitude + 1000])

plt.tight_layout()
plt.show()

# --- Salvando o arquivo .pcm ---

# Converter o sinal para inteiros de 16 bits
sinal_int16 = xd.astype(np.int16)

# Definir o nome do arquivo para refletir o novo sinal
nome_arquivo = 'impulso_processado.pcm'

# Salvar o arquivo .pcm
with open(nome_arquivo, 'wb') as f:
    f.write(sinal_int16.tobytes())

print(f'Sinal salvo como "{nome_arquivo}"')

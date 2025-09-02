import numpy as np
import matplotlib.pyplot as plt

# --- Defina o intervalo do sinal aqui ---
# O sinal x[n] será 1 para n_lower <= n <= n_upper
n_lower = -1
n_upper = 1
# -----------------------------------------

# Cria um vetor com todos os valores inteiros de n no intervalo
n_vec = np.arange(n_lower, n_upper + 1)

# Cria o vetor de frequência angular 'w' de -pi a pi
w = np.arange(-np.pi, np.pi, np.pi / 1000)

# Calcula a TFD de forma geral e eficiente
# np.outer(w, n_vec) cria uma matriz onde cada elemento (i, k) é w[i] * n_vec[k]
# Em seguida, calculamos o exponencial complexo para cada elemento
# Finalmente, somamos ao longo do eixo n (axis=1) para obter o valor de X para cada w
X = np.sum(np.exp(-1j * np.outer(w, n_vec)), axis=1)

# Calcula o Módulo (Magnitude) e a Fase de X
Mod_X = np.abs(X)
Fase_X = np.angle(X)

# --- Plotando o Módulo e a Fase ---

# Cria uma figura para os gráficos
plt.figure(figsize=(8, 6))

# Primeiro subplot (Magnitude)
plt.subplot(2, 1, 1)
plt.plot(w, Mod_X)
plt.title(f'Magnitude para n de {n_lower} a {n_upper}')
plt.xlabel('Frequência (w)')
plt.ylabel('Magnitude')
plt.grid(True)

# Segundo subplot (Fase)
plt.subplot(2, 1, 2)
plt.plot(w, Fase_X)
plt.title(f'Fase para n de {n_lower} a {n_upper}')
plt.xlabel('Frequência (w)')
plt.ylabel('Fase (radianos)')
plt.grid(True)

# Ajusta o layout para evitar sobreposição
plt.tight_layout()

# Mostra o gráfico
plt.show()
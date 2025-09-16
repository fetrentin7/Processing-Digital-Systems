import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
D1 = 3
a0 = 1.0
a1 = 1.0/3.0
N = 8  
n = np.arange(N)

# Entradas: impulso e degrau
x_delta = np.zeros(N)
x_delta[0] = 1.0
x_step = np.ones(N)

# Função para simular o sistema
def funcao(x, a0, a1, D1, N):
    y = np.zeros(N)
    for i in range(N):
        xi = x[i]
        fb = y[i - D1] if i - D1 >= 0 else 0.0
        y[i] = a0 * xi + a1 * fb
    return y

# Saídas
y_impulse = funcao(x_delta, a0, a1, D1, N)
y_step = funcao(x_step, a0, a1, D1, N)

# Gráfico - resposta ao impulso
plt.figure(figsize=(8,4))
plt.stem(n, y_impulse, basefmt=" ")
plt.title("Resposta ao impulso h[n]  (D1=3, a0=1, a1=1/3)")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid(True)
plt.show()

# Gráfico - resposta ao degrau
plt.figure(figsize=(8,4))
plt.stem(n, y_step, basefmt=" ")
plt.title("Resposta ao degrau y[n] para u[n]  (D1=3, a0=1, a1=1/3)")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(True)
plt.show()

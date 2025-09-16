import numpy as np
import matplotlib.pyplot as plt

D = [1, 1.5, 2]    # Numerador → zeros
Den = [1, 0, 0]    # Denominador → polos

# Calcula raízes
z = np.roots(D)    # Zeros
p = np.roots(Den)  # Polos

plt.figure(figsize=(6,6))
plt.plot(np.real(z), np.imag(z), 'bx', markersize=10, label='Zeros')
plt.plot(np.real(p), np.imag(p), 'ro', markersize=10, label='Polos')

# Marca multiplicidade dos polos na origem
plt.text(0.1, 0.1, '2x', fontsize=12, color='red')

# Adiciona eixos cartesianos
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)

# Configurações do gráfico
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.xlabel('Real')
plt.ylabel('Imaginário')
plt.title('Diagrama de Polos e Zeros')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

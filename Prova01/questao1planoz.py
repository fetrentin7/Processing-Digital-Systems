import numpy as np
import matplotlib.pyplot as plt

# parâmetros do sistema
a0 = 1
a1 = 0.5
D1 = 3

# polos (raízes da equação z^D1 = a1)
poles = [abs(a1)**(1/D1) * np.exp(1j*(np.angle(a1) + 2*np.pi*k)/D1) for k in range(D1)]
zeros = []  # não há zeros finitos

# gráfico
fig, ax = plt.subplots(figsize=(6,6))
# círculo unitário
theta = np.linspace(0,2*np.pi,400)
ax.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.5)

# polos e zeros
ax.scatter(np.real(poles), np.imag(poles), marker='x', color='red', s=100, label='Polos')
if zeros:
    ax.scatter(np.real(zeros), np.imag(zeros), marker='o', facecolors='none', edgecolors='blue', s=100, label='Zeros')

# eixos
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

ax.set_title(f"Polos (a1={a1}, D1={D1}) no plano-z")
ax.set_xlabel("Re(z)")
ax.set_ylabel("Im(z)")
ax.legend()
ax.set_aspect('equal')
ax.grid(True)
plt.show()

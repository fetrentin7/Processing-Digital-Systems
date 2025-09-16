import numpy as np
import matplotlib.pyplot as plt

R = 0.95

# Localização dos polos e zeros
zeros = [1]  # zero em z=1
poles = [R]  # polo em z=R

# Gráfico
fig, ax = plt.subplots(figsize=(6,6))

# círculo unitário
theta = np.linspace(0, 2*np.pi, 400)
ax.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.5)

# polos e zeros
ax.scatter(np.real(poles), np.imag(poles), marker='x', color='red', s=100, label='Polos')
ax.scatter(np.real(zeros), np.imag(zeros), marker='o', facecolors='none', edgecolors='blue', s=100, label='Zeros')

# eixos
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

ax.set_title(f"Polos e Zeros no Plano-Z (R={R})")
ax.set_xlabel("Re(z)")
ax.set_ylabel("Im(z)")
ax.legend()
ax.set_aspect('equal')
ax.grid(True)
plt.show()

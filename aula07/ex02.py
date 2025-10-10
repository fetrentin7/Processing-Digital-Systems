import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.patches import Circle

# --- 1. Coeficientes da Função de Transferência H(z) ---
# ===================================================================

# ===================================================================
b = [0.282, 0.282]  # Coeficientes do NUMERADOR
a = [ b, -0.4361]   # Coeficientes do DENOMINADOR
# ===================================================================

# Frequência de amostragem definida no problema
fs = 8000

# --- 2. Cálculo da Resposta em Frequência (usando freqz) ---
w, h = signal.freqz(b, a, fs=fs)

# --- 3. Plot da Resposta em Frequência em dB ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Converte o módulo da resposta para dB: 20*log10(|h|)
db = 20 * np.log10(np.abs(h))

ax1.plot(w, db, color='blue')
ax1.set_title('Resposta em Frequência do Filtro', fontsize=14)
ax1.set_xlabel('Frequência [Hz]')
ax1.set_ylabel('Módulo [dB]')
ax1.grid(True)
ax1.axhline(-3, color='r', linestyle='--', linewidth=0.8)
ax1.text(fs/4, -2.5, '-3 dB (frequência de corte)', color='r')

# --- 4. Cálculo e Plot dos Polos e Zeros ---
zeros = np.roots(b)
poles = np.roots(a)

unit_circle = Circle((0,0), 1, color='lightgray', fill=False, linestyle='--')
ax2.add_artist(unit_circle)

ax2.plot(np.real(zeros), np.imag(zeros), 'o', markersize=10, label='Zeros')
ax2.plot(np.real(poles), np.imag(poles), 'x', markersize=10, label='Polos')

ax2.set_title('Diagrama de Polos e Zeros', fontsize=14)
ax2.set_xlabel('Parte Real')
ax2.set_ylabel('Parte Imaginária')
ax2.grid(True)
ax2.axis('equal')
ax2.legend()
ax2.set_xlim([-1.5, 1.5])
ax2.set_ylim([-1.5, 1.5])

plt.tight_layout()
plt.show()
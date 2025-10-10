import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


numerator_coeffs = [0.7294, -2.1883, 2.1883, -0.7294]

denominator_coeffs = [1, -2.3741, 1.9294, -0.5321]


w, h = signal.freqz(numerator_coeffs, denominator_coeffs, worN=2048)


fig, axs = plt.subplots(2, 1, figsize=(10, 8))


magnitude_db = 20 * np.log10(np.abs(h))

axs[0].plot(w / np.pi, magnitude_db)
axs[0].set_title('Resposta em Frequência - Magnitude', fontsize=14)
axs[0].set_ylabel('Magnitude (dB)')
axs[0].set_xlabel('Frequência Normalizada (x $\pi$ rad/amostra)')
axs[0].grid(True)
axs[0].set_ylim(-60, 5) 

#Gráfico da Fase -

phase_rad = np.unwrap(np.angle(h))

# Plota a fase (em radianos) vs. a frequência normalizada
axs[1].plot(w / np.pi, phase_rad)
axs[1].set_title('Resposta em Frequência - Fase', fontsize=14)
axs[1].set_ylabel('Fase (radianos)')
axs[1].set_xlabel('Frequência Normalizada (x $\pi$ rad/amostra)')
axs[1].grid(True)


fig.tight_layout()


axs[0].set_xlabel('Frequência Normalizada (x $\pi$ rad/amostra)')
plt.show()
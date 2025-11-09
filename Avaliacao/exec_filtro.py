import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz, convolve

from hp_lp_coef import shelving_low, shelving_high, mf_peak  

# ============================
# Parâmetros gerais
# ============================
fs = 44100

# Filtros (valores de exemplo)
fc_lf = 200      # frequência de corte do low-shelf (Hz)
gain_lf = 6.0

fc_peak = 1000   # frequência central do peak (Hz)
fb_peak = 500    # largura de banda do peak (Hz)
gain_peak = 20.0 # ganho do peak (+ reforço / - corte)

fc_hf = 2000     # frequência de corte do high-shelf (Hz)
gain_hf = -10.0

# ============================
# Cálculo dos coeficientes
# ============================
b_lf, a_lf = shelving_low(fs, fc_lf, gain_lf)
b_peak, a_peak = mf_peak(fs, fc_peak, fb_peak, gain_peak)
b_hf, a_hf = shelving_high(fs, fc_hf, gain_hf)

# Combinação em série (convolução dos coeficientes)
b_combined = convolve(convolve(b_lf, b_peak), b_hf)
a_combined = convolve(convolve(a_lf, a_peak), a_hf)

# ============================
# Resposta em frequência
# ============================
w, H_lf = freqz(b_lf, a_lf, worN=4096, fs=fs)
_, H_peak = freqz(b_peak, a_peak, worN=4096, fs=fs)
_, H_hf = freqz(b_hf, a_hf, worN=4096, fs=fs)
_, H_combined = freqz(b_combined, a_combined, worN=4096, fs=fs)

plt.figure(figsize=(10,6))
plt.semilogx(w, 20 * np.log10(np.abs(H_lf)), linestyle='--', label='Low Shelving (200 Hz, +6 dB)')
plt.semilogx(w, 20 * np.log10(np.abs(H_peak)), linestyle='--', label='Mid Peak (1 kHz, +8 dB)')
plt.semilogx(w, 20 * np.log10(np.abs(H_hf)), linestyle='--', label='High Shelving (3 kHz, −9 dB)')

# Linha contínua e mais grossa para o EQ combinado
plt.semilogx(w, 20 * np.log10(np.abs(H_combined)), 'k', linewidth=2.2, label='Combined EQ')


plt.title('Equalizador em Série (Shelving + Peak Filters)')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Ganho (dB)')
plt.grid(which='both', linestyle=':', color='gray', alpha=0.7)
plt.legend()
plt.ylim(-24, 24)
plt.show()

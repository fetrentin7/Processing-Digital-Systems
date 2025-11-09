import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz
from hp_lp_coef import shelving_low, shelving_high, mf_peak

# ==========================
# Parâmetros gerais
# ==========================
FS = 44100
SWEEP_PATH = "Avaliacao/sweep_20_3k4.pcm"

GAIN_LF_DB = 6
GAIN_PEAK_DB = 10
GAIN_HF_DB = -6
FC_LF_HZ = 200
FC_PEAK_HZ = 1000
FB_PEAK_HZ = 400
FC_HF_HZ = 8000

# ==========================
# Leitura do sweep
# ==========================
sweep = np.fromfile(SWEEP_PATH, dtype=np.int16).astype(np.float32)
sweep /= np.max(np.abs(sweep))
t = np.linspace(0, len(sweep)/FS, len(sweep))
f = np.fft.rfftfreq(len(sweep), 1/FS)

# ==========================
# Cálculo dos coeficientes
# ==========================
b_lf, a_lf = shelving_low(FS, FC_LF_HZ, GAIN_LF_DB)
b_peak, a_peak = mf_peak(FS, FC_PEAK_HZ, FB_PEAK_HZ, GAIN_PEAK_DB)
b_hf, a_hf = shelving_high(FS, FC_HF_HZ, GAIN_HF_DB)

# ==========================
# Aplicação individual
# ==========================
y_lf = lfilter(b_lf, a_lf, sweep)
y_peak = lfilter(b_peak, a_peak, sweep)
y_hf = lfilter(b_hf, a_hf, sweep)

# ==========================
# Cascata — Equalizador completo
# ==========================
y_eq = lfilter(b_lf, a_lf, sweep)
y_eq = lfilter(b_peak, a_peak, y_eq)
y_eq = lfilter(b_hf, a_hf, y_eq)

# convolução:
b_eq = np.convolve(np.convolve(b_lf, b_peak), b_hf)
a_eq = np.convolve(np.convolve(a_lf, a_peak), a_hf)

# ==========================
# Respostas em frequência (freqz)
# ==========================
w, H_lf = freqz(b_lf, a_lf, worN=4096, fs=FS)
_, H_peak = freqz(b_peak, a_peak, worN=4096, fs=FS)
_, H_hf = freqz(b_hf, a_hf, worN=4096, fs=FS)
_, H_eq = freqz(b_eq, a_eq, worN=4096, fs=FS)

# ==========================
# Plot geral
# ==========================
fig, axs = plt.subplots(4, 2, figsize=(12, 12))
plt.suptitle("Validação do Equalizador — Filtros em Cascata com Sweep", fontsize=14)

# ---- 1. LOW-SHELF ----
axs[0,0].plot(t, sweep, color='gray', alpha=0.5)
axs[0,0].plot(t, y_lf, color='r')
axs[0,0].set_title("Low-Shelf - Domínio do Tempo")
axs[0,0].set_xlabel("Tempo [s]")
axs[0,0].set_ylabel("Amplitude")
axs[0,0].grid(True)

axs[0,1].semilogx(f, 20*np.log10(np.abs(np.fft.rfft(y_lf))+1e-9), color='r')
axs[0,1].semilogx(w, 20*np.log10(np.abs(H_lf)), '--', color='k', alpha=0.5, label='Teórica')
axs[0,1].set_title("Low-Shelf - Espectro")
axs[0,1].set_xlabel("Frequência [Hz]")
axs[0,1].set_ylabel("Magnitude [dB]")
axs[0,1].grid(True, which='both', linestyle=':')
axs[0,1].legend()

# ---- 2. PEAK ----
axs[1,0].plot(t, sweep, color='gray', alpha=0.5)
axs[1,0].plot(t, y_peak, color='g')
axs[1,0].set_title("Peak - Domínio do Tempo")
axs[1,0].set_xlabel("Tempo [s]")
axs[1,0].set_ylabel("Amplitude")
axs[1,0].grid(True)

axs[1,1].semilogx(f, 20*np.log10(np.abs(np.fft.rfft(y_peak))+1e-9), color='g')
axs[1,1].semilogx(w, 20*np.log10(np.abs(H_peak)), '--', color='k', alpha=0.5, label='Teórica')
axs[1,1].set_title("Peak - Espectro")
axs[1,1].set_xlabel("Frequência [Hz]")
axs[1,1].set_ylabel("Magnitude [dB]")
axs[1,1].grid(True, which='both', linestyle=':')
axs[1,1].legend()

# ---- 3. HIGH-SHELF ----
axs[2,0].plot(t, sweep, color='gray', alpha=0.5)
axs[2,0].plot(t, y_hf, color='b')
axs[2,0].set_title("High-Shelf - Domínio do Tempo")
axs[2,0].set_xlabel("Tempo [s]")
axs[2,0].set_ylabel("Amplitude")
axs[2,0].grid(True)

axs[2,1].semilogx(f, 20*np.log10(np.abs(np.fft.rfft(y_hf))+1e-9), color='b')
axs[2,1].semilogx(w, 20*np.log10(np.abs(H_hf)), '--', color='k', alpha=0.5, label='Teórica')
axs[2,1].set_title("High-Shelf - Espectro")
axs[2,1].set_xlabel("Frequência [Hz]")
axs[2,1].set_ylabel("Magnitude [dB]")
axs[2,1].grid(True, which='both', linestyle=':')
axs[2,1].legend()

# ---- 4. EQUALIZADOR COMPLETO ----
axs[3,0].plot(t, sweep, color='gray', alpha=0.5, label='Entrada (sweep)')
axs[3,0].plot(t, y_eq, color='black', label='Saída Equalizada')
axs[3,0].set_title("Equalizador Completo - Domínio do Tempo")
axs[3,0].set_xlabel("Tempo [s]")
axs[3,0].set_ylabel("Amplitude")
axs[3,0].legend()
axs[3,0].grid(True)

axs[3,1].semilogx(f, 20*np.log10(np.abs(np.fft.rfft(y_eq))+1e-9), color='black', label='Saída')
axs[3,1].semilogx(w, 20*np.log10(np.abs(H_eq)), '--', color='gray', alpha=0.6, label='Teórica (Cascata)')
axs[3,1].set_title("Equalizador Completo - Espectro de Saída")
axs[3,1].set_xlabel("Frequência [Hz]")
axs[3,1].set_ylabel("Magnitude [dB]")
axs[3,1].grid(True, which='both', linestyle=':')
axs[3,1].legend()

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()


# Exporta o resultado PCM final

y_eq = y_eq / np.max(np.abs(y_eq))
np.int16(y_eq * 32767).tofile("saida_equalizador.pcm")


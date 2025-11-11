import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz
from hp_lp_coef import shelving_low, shelving_high, mf_peak

# ==========================
# Parâmetros do áudio
# ==========================
FS = 44100           # taxa de amostragem
SWEEP_PATH = "Avaliacao/sweep_20_3k4.pcm"  # caminho do sweep

# Leitura do sweep PCM 16-bit little endian
sweep = np.fromfile(SWEEP_PATH, dtype=np.int16).astype(np.float32)
sweep /= np.max(np.abs(sweep))  # normaliza entre -1 e 1
t = np.linspace(0, len(sweep)/FS, len(sweep))

# ==========================
# Parâmetros dos filtros
# ==========================
GAIN_LF_DB = 6
GAIN_PEAK_DB = 10
GAIN_HF_DB = -6

FC_LF_HZ = 200
FC_PEAK_HZ = 1000
FB_PEAK_HZ = 400
FC_HF_HZ = 8000

# ==========================
# Cálculo dos coeficientes
# ==========================
b_lf, a_lf = shelving_low(FS, FC_LF_HZ, GAIN_LF_DB)
b_peak, a_peak = mf_peak(FS, FC_PEAK_HZ, FB_PEAK_HZ, GAIN_PEAK_DB)
b_hf, a_hf = shelving_high(FS, FC_HF_HZ, GAIN_HF_DB)

# Aplicação dos filtros individualmente

y_lf = lfilter(b_lf, a_lf, sweep)
y_peak = lfilter(b_peak, a_peak, sweep)
y_hf = lfilter(b_hf, a_hf, sweep)

# ==========================
# Visualização
# ==========================
fig, axs = plt.subplots(3, 2, figsize=(12, 9))
plt.suptitle("Validação dos Filtros com Sweep de 20 Hz a 3.4 kHz", fontsize=14)

# ---- Filtro Low-Shelf ----
axs[0,0].plot(t, sweep, color='gray', alpha=0.5, label='Entrada (sweep)')
axs[0,0].plot(t, y_lf, color='r', label='Saída filtrada')
axs[0,0].set_title("Filtro Low-Shelf - Domínio do Tempo")
axs[0,0].set_xlabel("Tempo [s]")
axs[0,0].set_ylabel("Amplitude")
axs[0,0].legend()
axs[0,0].grid(True)

# Espectro de magnitude
f = np.fft.rfftfreq(len(sweep), 1/FS)
axs[0,1].semilogx(f, 20*np.log10(np.abs(np.fft.rfft(y_lf))+1e-9), color='r')
axs[0,1].set_title("Low-Shelf - Espectro de Saída")
axs[0,1].set_xlabel("Frequência [Hz]")
axs[0,1].set_ylabel("Magnitude [dB]")
axs[0,1].grid(True, which='both', linestyle=':')

# ---- Filtro Peak ----
axs[1,0].plot(t, sweep, color='gray', alpha=0.5)
axs[1,0].plot(t, y_peak, color='g')
axs[1,0].set_title("Filtro Peak - Domínio do Tempo")
axs[1,0].set_xlabel("Tempo [s]")
axs[1,0].set_ylabel("Amplitude")
axs[1,0].grid(True)

axs[1,1].semilogx(f, 20*np.log10(np.abs(np.fft.rfft(y_peak))+1e-9), color='g')
axs[1,1].set_title("Peak - Espectro de Saída")
axs[1,1].set_xlabel("Frequência [Hz]")
axs[1,1].set_ylabel("Magnitude [dB]")
axs[1,1].grid(True, which='both', linestyle=':')

# ---- Filtro High-Shelf ----
axs[2,0].plot(t, sweep, color='gray', alpha=0.5)
axs[2,0].plot(t, y_hf, color='b')
axs[2,0].set_title("Filtro High-Shelf - Domínio do Tempo")
axs[2,0].set_xlabel("Tempo [s]")
axs[2,0].set_ylabel("Amplitude")
axs[2,0].grid(True)

axs[2,1].semilogx(f, 20*np.log10(np.abs(np.fft.rfft(y_hf))+1e-9), color='b')
axs[2,1].set_title("High-Shelf - Espectro de Saída")
axs[2,1].set_xlabel("Frequência [Hz]")
axs[2,1].set_ylabel("Magnitude [dB]")
axs[2,1].grid(True, which='both', linestyle=':')

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()



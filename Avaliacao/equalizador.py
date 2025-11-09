from hp_lp_coef import shelving_low, shelving_high
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, chirp, freqz
from scipy.fft import rfft, rfftfreq

# ============================
fs = 44100
t = np.linspace(0, 5, int(5*fs))
sweep = chirp(t, f0=20, f1=fs/2, t1=5, method='logarithmic')
sweep /= np.max(np.abs(sweep))


b_lf, a_lf = shelving_low(fs, 200, 8)
b_hf, a_hf = shelving_high(fs, 8000, 8)

s_lf = lfilter(b_lf, a_lf, sweep)
s_hf = lfilter(b_hf, a_hf, sweep)


def compute_spectrum(signal, fs):
    N = len(signal)
    freqs = rfftfreq(N, 1/fs)
    mag = 20 * np.log10(np.abs(rfft(signal)) + 1e-9)
    return freqs, mag

freqs, mag_in = compute_spectrum(sweep, fs)
_, mag_lf = compute_spectrum(s_lf, fs)
_, mag_hf = compute_spectrum(s_hf, fs)


w_lf, h_lf = freqz(b_lf, a_lf, worN=2048)
w_hf, h_hf = freqz(b_hf, a_hf, worN=2048)
freqz_lf = w_lf * fs / (2 * np.pi)
freqz_hf = w_hf * fs / (2 * np.pi)
H_lf_dB = 20 * np.log10(np.abs(h_lf))
H_hf_dB = 20 * np.log10(np.abs(h_hf))


plt.figure(figsize=(10, 7))

# Cria dois gráficos (2 linhas, 1 coluna)
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# --- LOW-SHELF ---
axs[0].semilogx(freqs, mag_in, label="Input (Sweep)", color="C0", alpha=0.6)
axs[0].semilogx(freqs, mag_lf, label="Low-shelf (real)", color="C1")
axs[0].semilogx(freqz_lf, H_lf_dB + mag_in.max() - H_lf_dB.max(),
                "--", color="C1", alpha=0.8, label="Low-shelf (teórica)")
axs[0].set_title("Low-Shelf: resposta real (FFT) vs teórica (freqz)")
axs[0].set_xlabel("Frequência [Hz]")
axs[0].set_ylabel("Magnitude [dB]")
axs[0].grid(True, which="both")
axs[0].legend()
axs[0].set_xlim(20, 8000)

# --- HIGH-SHELF ---
axs[1].semilogx(freqs, mag_in, label="Input (Sweep)", color="C0", alpha=0.6)
axs[1].semilogx(freqs, mag_hf, label="High-shelf (real)", color="C2")
axs[1].semilogx(freqz_hf, H_hf_dB + mag_in.max() - H_hf_D B.max(),
                "--", color="C2", alpha=0.8, label="High-shelf (teórica)")
axs[1].set_title("High-Shelf: resposta real (FFT) vs teórica (freqz)")
axs[1].set_xlabel("Frequência [Hz]")
axs[1].set_ylabel("Magnitude [dB]")
axs[1].grid(True, which="both")
axs[1].legend()
axs[1].set_xlim(20, 8000)

plt.tight_layout()
plt.show()

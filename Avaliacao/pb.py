import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# --- Parâmetros ---
fs = 48000
fc = 500
G = 10  #(+ para boost, - para cut)

A = 10**(G/20)
H0 = A - 1
wc = 2 * np.pi * fc / fs

aB = (np.sin(wc) - np.cos(wc)) / (np.sin(wc) + np.cos(wc))
C = np.sqrt(A)

# --- Filtro all-pass ---
# A(z) = (z^-1 + aB/C) / (1 + (aB/C) z^-1)
b_ap = np.array([1, aB/C])
a_ap = np.array([1, (aB/C)])


w, A_z = signal.freqz(b_ap, a_ap, worN=2048)
H = 1 + (H0/2) * (1 + A_z)  # Low-shelf (+)
H_dB = 20*np.log10(abs(H))

f = w * fs / (2*np.pi)
plt.figure(figsize=(8,4))
plt.semilogx(f, H_dB)
plt.title("Low-Shelving Filter (1st-order all-pass method)")
plt.xlabel("Frequência [Hz]")
plt.ylabel("Ganho [dB]")
plt.grid(True, which='both', ls='--')
plt.axvline(fc, color='r', linestyle='--', label=f"fc={fc}Hz")
plt.axhline(G, color='g', linestyle=':')
plt.legend()
plt.show()

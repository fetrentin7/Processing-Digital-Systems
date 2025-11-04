import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

def low_shelf_coeffs(fs, fc, G_db):
    A  = 10**(G_db/20)
    k  = (A - 1)/2
    wc = 2*np.pi*fc/fs
    aB = (np.sin(wc) - np.cos(wc)) / (np.sin(wc) + np.cos(wc))

    b0 = 1 + k*(1 + aB)
    b1 = aB + k*(1 + aB)
    a0 = 1.0
    a1 = aB
    # forma direta H(z) = (b0 + b1 z^-1) / (1 + a1 z^-1)
    b = np.array([b0, b1])
    a = np.array([1.0, a1])
    return b, a

def plot_response(fs, b, a, label):
    w, h = freqz(b, a, worN=2048)
    f = w*fs/(2*np.pi)
    plt.semilogx(f, 20*np.log10(np.abs(h)), label=label)


fs, fc = 44100, 1000

b_boost, a_boost = low_shelf_coeffs(fs, fc, +10)
b_cut,   a_cut   = low_shelf_coeffs(fs, fc, -10)

plt.figure(figsize=(8,4))
plot_response(fs, b_boost, a_boost, "Low-shelf boost (+6 dB)")
plot_response(fs, b_cut,   a_cut,   "Low-shelf cut (-6 dB)")
plt.axvline(fc, linestyle="--")
plt.xlabel("Frequência [Hz]"); plt.ylabel("Ganho [dB]")
plt.title("Low-shelf (passa-baixas) — boost e cut")
plt.grid(True, which="both", ls="--"); plt.legend(); plt.show()

print("Boost coeffs b,a:", b_boost, a_boost)
print("Cut   coeffs b,a:", b_cut, a_cut)



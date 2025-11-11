import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

def shelving_low(fs, fc, G):
    V0 = 10**(G/20)
    K = np.tan(np.pi * fc / fs)

    if G >= 0:
        aB = (K - 1) / (K + 1)
    else:
        aB = (K - V0) / (K + V0)

    k = (V0 - 1)/2
    b0 = 1 + k*(1 + aB)
    b1 = aB + k*(1 + aB)
    a0 = 1
    a1 = aB

    b = np.array([b0, b1])
    a = np.array([a0, a1])
    return b, a


def shelving_high(fs, fc, G):
    V0 = 10**(G/20)
    K_H0 = (V0 - 1) / 2
    K = np.tan(np.pi * fc / fs)


    if G >= 0: # Boost (Reforço)
        aB = (K - 1) / (K + 1)
    else: # Cut (Atenuação)
        aB = (V0 * K - 1) / (V0 * K + 1)

    b0 = 1 + K_H0 * (1 - aB)
    b1 = aB + K_H0 * (aB - 1)
    a0 = 1
    a1 = aB

    b = np.array([b0, b1])
    a = np.array([a0, a1])
    return b, a

def mf_peak(fs, fc, fb, G):
    V0 = 10**(G / 20.0)    # ganho linear
    H0 = V0 - 1
    K_H0 = H0 / 2

    d = -np.cos(2 * np.pi * fc / fs)  # controla f0
    tan_bw = np.tan(np.pi * fb / fs)  # controla largura da banda

    # Coeficientes da transformação bilinear
    if G >= 0:
        a_BC = (tan_bw - 1) / (tan_bw + 1)      # boost
    else:
        a_BC = (tan_bw - V0) / (tan_bw + V0)    # cut

    # Denominador
    a0 = 1.0
    a1 = d * (1 - a_BC)
    a2 = -a_BC

    # Numerador 
    b0 = 1 + K_H0 * (1 + a_BC)
    b1 = d * (1 - a_BC)
    b2 = -a_BC * (1 + K_H0) - K_H0

    # Normalização
    b = np.array([b0, b1, b2])
    a = np.array([a0, a1, a2])
    return b / a[0], a / a[0]

if __name__ == "__main__":  
    fs = 44100
    fc_low = 1000
    fc_high = 1000
    fc = 1000     
    fb = 500      
    fig, axs = plt.subplots(3, 1, figsize=(8, 8))

    for G in [10, -10]:
        b, a = shelving_low(fs, fc_low, G)
        w, h = freqz(b, a, worN=2048)
        axs[0].semilogx(w * fs / (2 * np.pi), 20 * np.log10(abs(h)), label=f"G={G} dB")

    axs[0].set_title("Filtro Low-Shelf (boost/cut)")
    axs[0].set_xlabel("Frequência [Hz]")
    axs[0].set_ylabel("Ganho [dB]")
    axs[0].axvline(fc_low, color='r', ls='--', alpha=0.5)
    axs[0].grid(True, which='both')
    axs[0].legend()

    # ---------- HIGH-SHELF ----------
    for G in [10, -10]:
        b, a = shelving_high(fs, fc_high, G)
        w, h = freqz(b, a, worN=2048)
        axs[1].semilogx(w * fs / (2 * np.pi), 20 * np.log10(abs(h)), label=f"G={G} dB")

    axs[1].set_title("Filtro High-Shelf (boost/cut)")
    axs[1].set_xlabel("Frequência [Hz]")
    axs[1].set_ylabel("Ganho [dB]")
    axs[1].axvline(fc_high, color='b', ls='--', alpha=0.5)
    axs[1].grid(True, which='both')
    axs[1].legend()


    for G in [10, -10]:
        b, a = mf_peak(fs, fc, fb, G)
        w, h = freqz(b, a, worN=2048)
        axs[2].semilogx(w * fs / (2 * np.pi), 20*np.log10(abs(h)), label=f"G={G} dB")

    axs[2].set_title("Filtro Peak (boost/cut)")
    axs[2].set_xlabel("Frequência [Hz]")
    axs[2].set_ylabel("Ganho [dB]")
    axs[2].axvline(fc, color='g', ls='--', alpha=0.5)
    axs[2].grid(True, which='both')
    axs[2].legend()

    plt.tight_layout()
    plt.show()
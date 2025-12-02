import numpy as np
import matplotlib.pyplot as plt

def separa_coef(lista):
    
    par = lista[0::2]
    impar = lista[1::2]

    return par, impar

def fft(x):

    x = np.array(x, dtype=complex)

    N = x.size

    if N <= 1:
        return x
    
    x_par, x_impar = separa_coef(x)
    coef_par = fft(x_par)
    coef_impar = fft(x_impar)
    resultado = np.zeros(N, dtype=complex)
    for k in range(N // 2):
        W_k = np.exp(-2j * np.pi * k / N)
        resultado[k] = coef_par[k] + W_k * coef_impar[k]
        resultado[k + N//2] = coef_par[k] - W_k * coef_impar[k]
    return resultado



data = np.fromfile("TrabalhoM3/sweep-1.pcm", dtype=np.int16)

# Normaliza para [-1,1]
x = data.astype(np.float32) / 32768.0

# FFT
y = fft(x)
N = len(x)
fs = 48000  # ou 44100... depende do arquivo!

freqs = np.fft.fftfreq(N, 1/fs)

plt.figure(figsize=(12,6))
plt.plot(freqs[:N//2], np.abs(y[:N//2]))
plt.title("FFT do sweep1-pcm")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
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



fs = 1000              #
T = 1                  
N = fs * T             

t = np.linspace(0, T, N, endpoint=False)
freq_sinal = 50        # Hz

# seno de 50 Hz
x = np.sin(2 * np.pi * freq_sinal * t)

# ---------- FFT ----------
y = fft(x)

# ---------- FREQUÊNCIAS ----------
freqs = np.fft.fftfreq(N, 1/fs)


plt.figure(figsize=(12, 6))
plt.plot(freqs[:N//2], np.abs(y[:N//2]), label="Magnitude FFT")
plt.title("Espectro do Sinal (FFT)")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
import numpy as np
from scipy import signal

# Coeficientes do filtro
num = [0.7294, -2.1883, 2.1883, -0.7294]
den = [1, -2.3741, 1.9294, -0.5321]
fs = 8000

freqs_to_test = np.array([100, 1000])

w, h = signal.freqz(num, den, worN=fs, fs=fs) # worN grande para boa precisão

for f in freqs_to_test:
    # Encontra o índice no array de frequências 'w' mais próximo de 'f'
    idx = np.argmin(np.abs(w - f))
    
    # Pega a magnitude da resposta nesse ponto
    magnitude = np.abs(h[idx])
    
    # Converte para dB
    attenuation_db = 20 * np.log10(magnitude)
    
    print(f"Atenuação Teórica em {f} Hz: {attenuation_db:.2f} dB")
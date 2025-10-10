import numpy as np
from scipy.io import wavfile
from scipy import signal


num = [0.7294, -2.1883, 2.1883, -0.7294]
den = [1, -2.3741, 1.9294, -0.5321]


fs = 8000

tamanho_impulso = 512
impulso = np.zeros(tamanho_impulso)
impulso[0] = 1


resposta_impulso = signal.lfilter(num, den, impulso)

# 3. Normaliza o resultado para o pico máximo ser 1.0
resposta_impulso /= np.max(np.abs(resposta_impulso))

# 4. Salva a resposta como um arquivo WAV em 32-bit float
wavfile.write('resposta_impulso.wav', fs, resposta_impulso.astype(np.float32))



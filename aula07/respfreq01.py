import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
import matplotlib.pyplot as plt
from scipy.signal import freqz

def get_coeffs_from_user(prompt):
    while True:
        try:
            input_str = input(prompt)
            coeffs = [float(item) for item in input_str.split(',')]
            return coeffs
        except ValueError:
            print("Entrada inválida. Por favor, insira números separados por vírgula.")

# --- 1. Obter os coeficientes do usuário ---
print("Digite os coeficientes dos polinômios da sua função de transferência H(z).")
print("Exemplo: para o polinômio z² - 0.9z + 0.2, digite: 1, -0.9, 0.2")

num = get_coeffs_from_user("Coeficientes do NUMERADOR (num): ")
den = get_coeffs_from_user("Coeficientes do DENOMINADOR (den): ")


# Define a frequência de amostragem (em Hz)
fs = 8000  # Exemplo: 1000 Hz

# ===================================================================
# PARTE 1: CÁLCULO E PLOTAGEM DOS PÓLOS E ZEROS
# ===================================================================

# Calcular os pólos e zeros
zeros = np.roots(num)
poles = np.roots(den)

print("\n--- Resultados ---")
print(f"Zeros encontrados em: {zeros}")
print(f"Pólos encontrados em: {poles}")
print("--------------------")

# Criar o gráfico do Plano Z
fig_pz, ax_pz = plt.subplots(figsize=(7, 7))
fig_pz.suptitle('Plano Z', fontsize=16)

# Desenha o Círculo Unitário
theta = np.linspace(0, 2*np.pi, 100)
ax_pz.plot(np.cos(theta), np.sin(theta), 'k--', label='Círculo Unitário', alpha=0.5)

# Plota os Zeros ('o') e Pólos ('x')
if len(zeros) > 0:
    ax_pz.plot(np.real(zeros), np.imag(zeros), 'o', markersize=10, c='b', label='Zeros')
if len(poles) > 0:
    ax_pz.plot(np.real(poles), np.imag(poles), 'x', markersize=12, mew=2, c='r', label='Pólos')

# Formatação do Gráfico do Plano Z
ax_pz.axhline(0, color='grey', lw=0.5)
ax_pz.axvline(0, color='grey', lw=0.5)
ax_pz.set_xlabel('Eixo Real')
ax_pz.set_ylabel('Eixo Imaginário')
ax_pz.set_title('Localização dos Pólos e Zeros')
ax_pz.set_aspect('equal')
ax_pz.grid(True)
ax_pz.legend()
limit = max(1.5, np.max(np.abs(poles))*1.2 if len(poles)>0 else 1.5, np.max(np.abs(zeros))*1.2 if len(zeros)>0 else 1.5)
ax_pz.set_xlim(-limit, limit)
ax_pz.set_ylim(-limit, limit)

# ===================================================================
# PARTE 2: CÁLCULO E PLOTAGEM DA RESPOSTA EM FREQUÊNCIA (em Hz)
# ===================================================================

# Calcula a resposta em frequência.
# freqz retorna: w (frequências angulares em rad/amostra) e h (resposta complexa)
w, h = freqz(num, den, worN=2048)

# Converte w de rad/amostra para Hz
frequencies_hz = (w / (2 * np.pi)) * fs

# Cria a figura para a resposta em frequência em Hz
fig_freq_hz, axs_freq_hz = plt.subplots(2, 1, figsize=(10, 8))
fig_freq_hz.suptitle('Resposta em Frequência (em Hz)', fontsize=16)

# --- Gráfico da Magnitude (em Hz) ---
# Converte a magnitude para decibéis (dB)
magnitude_db = 20 * np.log10(np.abs(h) + 1e-9) # Adiciona um valor pequeno para evitar log(0)

# Plota a magnitude. O eixo X agora está em Hz
axs_freq_hz[0].plot(frequencies_hz, magnitude_db)
axs_freq_hz[0].set_title('Magnitude')
axs_freq_hz[0].set_xlabel('Frequência (Hz)')
axs_freq_hz[0].set_ylabel('Magnitude (dB)')
axs_freq_hz[0].grid(True)


# --- Gráfico da Fase (em Hz) ---
# Extrai a fase e a "desembrulha" para evitar saltos de 2π
phase = np.unwrap(np.angle(h))

axs_freq_hz[1].plot(frequencies_hz, phase)
axs_freq_hz[1].set_title('Fase')
axs_freq_hz[0].set_xlabel('Frequência (Hz)')
axs_freq_hz[1].set_ylabel('Fase (radianos)')
axs_freq_hz[1].grid(True)


# ===================================================================
# PARTE 3: CÁLCULO E PLOTAGEM DA RESPOSTA EM FREQUÊNCIA (Normalizada)
# ===================================================================


# Cria a figura para a resposta em frequência normalizada
fig_freq_norm, axs_freq_norm = plt.subplots(2, 1, figsize=(10, 8))
fig_freq_norm.suptitle('Resposta em Frequência (Normalizada)', fontsize=16)

# --- Gráfico da Magnitude (Normalizada) ---
# Magnitude is already in dB
# magnitude_db = 20 * np.log10(np.abs(h) + 1e-9) # Already calculated

# Plota a magnitude. O eixo X agora está em Frequência Normalizada
axs_freq_norm[0].plot(w / np.pi, magnitude_db)
axs_freq_norm[0].set_title('Magnitude')
axs_freq_norm[0].set_xlabel('Frequência Normalizada (x π rad/amostra)')
axs_freq_norm[0].set_ylabel('Magnitude (dB)')
axs_freq_norm[0].grid(True)


# --- Gráfico da Fase (Normalizada) ---
# Phase is already unwrapped
# phase = np.unwrap(np.angle(h)) # Already calculated

axs_freq_norm[1].plot(w / np.pi, phase)
axs_freq_norm[1].set_title('Fase')
axs_freq_norm[1].set_xlabel('Frequência Normalizada (x π rad/amostra)')
axs_freq_norm[1].set_ylabel('Fase (radianos)')
axs_freq_norm[1].grid(True)


# Exibe todos os gráficos
plt.tight_layout(rect=[0, 0, 1, 0.96]) # Ajusta o layout para o supertítulo
plt.show()
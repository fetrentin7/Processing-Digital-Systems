import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

def media_movel_coef(k):
    """Retorna os coeficientes do filtro de média móvel de ordem k."""
    return np.ones(k) / k

if __name__ == "__main__":
    FC = 0.14  # frequência de corte (entre 0 e 0.5)
    M = 100    # comprimento do filtro (101 pontos)
    N = M + 1  # número de coeficientes

    # --- Sweep de frequência ---
    n_amostras = 1111110
    n = np.arange(n_amostras)
    frequencias = np.linspace(0, 0.5, 100)
    amplitude_saida = []

    k_janela = 10  # tamanho da janela da média móvel
    h_mm = media_movel_coef(k_janela)

    for freq in frequencias:
        x = np.sin(2 * np.pi * freq * n)
        y = np.convolve(x, h_mm, mode='full')[:n_amostras]
        # Calcula a amplitude RMS da saída na segunda metade (para evitar transientes)
        rms_y = np.sqrt(np.mean(y[n_amostras//2:]**2))
        amplitude_saida.append(rms_y)

    # Normaliza para amplitude máxima 1 (como em saida.py)
    amplitude_saida = np.array(amplitude_saida) / np.max(amplitude_saida)

    plt.figure(figsize=(10, 5))
    plt.plot(frequencias, amplitude_saida)
    plt.axvline(1/k_janela, color='r', linestyle='--', label=f'Aproximada FC (1/k={1/k_janela:.2f})')
    plt.title('Resposta em Frequência do Filtro de Média Móvel (Sweep)')
    plt.xlabel('Frequência Normalizada (ciclos/amostra)')
    plt.ylabel('Amplitude Normalizada')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
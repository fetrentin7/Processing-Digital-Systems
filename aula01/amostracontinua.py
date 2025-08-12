import numpy as np
import matplotlib.pyplot as plt


def main():

    amplitude = 16384
    dt = 5e-5  # Corresponde a Dt = 5*10^-5
    t = np.arange(-5e-3, 5e-3 + dt, dt)  # Corresponde a t = -5*10^-3:Dt:5*10^-3


    f = 1000  # Frequência em Hz
    xa = np.cos(2 * np.pi * f * t)  # Corresponde a xa = cos(2*pi*f*t)


    fs = 8000  # Frequência de amostragem em Hz
    ts = 1 / fs  # Período de amostragem


    n = np.arange(-20, 21, 1)  # Corresponde a n = -20:1:20
    # Calcula o sinal discreto (amostrado)
    xd = amplitude * np.cos(2  * np.pi * n * f / fs)


    plt.figure(figsize=(10, 8))


    ax1 = plt.subplot(2, 1, 1)

    # Plota o sinal "analógico"
    ax1.plot(t * 1000 , xa, label='Sinal "Analógico" xa(t)')

    ax1.stem(n * ts * 1000, xd, linefmt='r-', markerfmt='ro', basefmt='r-', label='Amostras x[n]')

    # Configurações do primeiro gráfico
    ax1.set_xlabel('Tempo [ms]')
    ax1.set_ylabel('Amplitude')
    ax1.set_title(f'Sinal de Frequência = {f} Hz e Amostragem com Fs = {fs} Hz')
    ax1.grid(True)
    ax1.legend()  # Adiciona a legenda


    ax2 = plt.subplot(2, 1, 2)


    ax2.stem(n, xd)

    # Configurações do segundo gráfico
    ax2.set_xlabel('Índice da Amostra (n)')
    ax2.set_ylabel('Amplitude x[n]')
    ax2.set_title('Sinal Amostrado (Domínio Discreto)')
    ax2.grid(True)

    # Ajusta o layout para evitar sobreposição de títulos e eixos
    plt.tight_layout()

    # Exibe os gráficos
    plt.show()




# Ponto de entrada do script
if __name__ == '__main__':
    main()
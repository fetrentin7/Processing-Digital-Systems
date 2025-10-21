import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import os
# --- PARÂMETROS GLOBAIS ---
COEFFS_FILENAME = "coeficientes.txt"
PI = np.pi # Usar o PI do numpy para maior precisão

def design_and_save_filter(filename):
    """
    Projeta um filtro FIR Passa-Baixas com janela de Hamming e salva os coeficientes.
    Esta função é baseada na lógica do seu código original.
    """
    print(f"Projetando um novo filtro e salvando em '{filename}'...")
    # Parâmetros de design
    FC = 0.14  # Frequência de corte normalizada (entre 0 e 0.5)
    M = 100    # Comprimento do filtro (resulta em 101 coeficientes)
    N = M + 1  # Número de coeficientes

    # Inicializa o vetor do filtro
    h = np.zeros(N)

    # Lógica para criar a resposta ao impulso (sinc)
    for i in range(N):
        x = i - M / 2
        if x == 0:
            h[i] = 2 * PI * FC
        else:
            h[i] = np.sin(2 * PI * FC * x) / x
        # Aplica a janela de Hamming
        h[i] *= (0.54 - 0.46 * np.cos(2 * PI * i / M))

    # Normaliza para ganho unitário em DC (ganho de 1 para frequência zero)
    soma = np.sum(h)
    h = h / soma

    # Salva os coeficientes no arquivo de texto
    np.savetxt(filename, h, fmt="%.10f")
    print("Filtro projetado com sucesso.")
    return h

def main():
    """
    Função principal que carrega o filtro e aplica a um sinal PCM.
    """
    # --- 1. CARREGAR OU GERAR OS COEFICIENTES DO FILTRO ---
    if not os.path.exists(COEFFS_FILENAME):
        print(f"Arquivo de coeficientes '{COEFFS_FILENAME}' não encontrado.")
        num_coeffs = design_and_save_filter(COEFFS_FILENAME)
    else:
        print(f"Carregando coeficientes do filtro de '{COEFFS_FILENAME}'...")
        num_coeffs = np.loadtxt(COEFFS_FILENAME)

    # O denominador de um filtro FIR é sempre [1.0]
    den_coeffs = [1.0]

    # --- 2. OBTER ARQUIVOS DE ENTRADA/SAÍDA DO USUÁRIO ---
    input_pcm_file = input("Digite o nome do arquivo .pcm de ENTRADA: ")
    output_pcm_file = input("Digite o nome do arquivo .pcm de SAÍDA: ")

    if not os.path.exists(input_pcm_file):
        print(f"\nERRO: Arquivo de entrada '{input_pcm_file}' não encontrado.")
        return

    # --- 3. LER SINAL DE ENTRADA E APLICAR FILTRO ---
    print("\nLendo sinal de entrada...")
    # Lê o arquivo binário como uma sequência de inteiros de 16 bits
    input_signal = np.fromfile(input_pcm_file, dtype=np.int16)

    print("Aplicando o filtro...")
    # Aplica o filtro FIR ao sinal de entrada.
    # É importante fazer os cálculos em float para manter a precisão.
    filtered_signal = signal.lfilter(num_coeffs, den_coeffs, input_signal.astype(np.float64))

    # --- 4. PLOTAR O PASSO A PASSO ---
    print("Gerando gráficos...")
    fig, axs = plt.subplots(3, 1, figsize=(12, 12))
    fig.suptitle('Análise do Processo de Filtragem', fontsize=16)

    # Gráfico 1: Sinal Original
    axs[0].plot(input_signal, label='Sinal Original')
    axs[0].set_title('1. Sinal de Entrada Original')
    axs[0].set_xlabel('Amostras')
    axs[0].set_ylabel('Amplitude')
    axs[0].legend()
    axs[0].grid(True)

    # Gráfico 2: Coeficientes do Filtro
    axs[1].plot(num_coeffs)
    axs[1].set_title('2. Coeficientes do Filtro (Resposta ao Impulso)')
    axs[1].set_xlabel('Amostras')
    axs[1].set_ylabel('Amplitude')
    axs[1].grid(True)

    # Gráfico 3: Sinal Filtrado
    axs[2].plot(filtered_signal, label='Sinal Filtrado', color='orange')
    axs[2].set_title('3. Sinal de Saída Filtrado')
    axs[2].set_xlabel('Amostras')
    axs[2].set_ylabel('Amplitude')
    axs[2].legend()
    axs[2].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.96])
    plt.show()

    # --- 5. GERAR ARQUIVO .PCM DE SAÍDA ---
    print("\nSalvando sinal filtrado...")
    # Converte o sinal de float de volta para int16 antes de salvar
    # Adiciona clipping para evitar overflow
    filtered_signal_int16 = np.clip(filtered_signal, -32768, 32767).astype(np.int16)

    # Salva o array de amostras filtradas em um novo arquivo binário
    filtered_signal_int16.tofile(output_pcm_file)
    print(f"Arquivo filtrado salvo com sucesso como '{output_pcm_file}'.")

# --- Executa o programa ---
if __name__ == "__main__":
    main()
import numpy as np
import matplotlib.pyplot as plt
import struct

def media_movel(vetor_entrada, k):
    """
    Aplica um filtro de média móvel a um vetor de entrada.

    Esta função simula um filtro digital onde a saída é a média das 'k'
    amostras de entrada mais recentes.

    Args:
        vetor_entrada (list or np.array): O sinal de entrada com n valores.
        k (int): O tamanho da janela da média móvel (o número de amostras).

    Returns:
        list: O sinal de saída filtrado.
    """
    # Validação para garantir que k seja um inteiro positivo
    if not isinstance(k, int) or k <= 0:
        raise ValueError("O tamanho da janela (k) deve ser um inteiro positivo.")

    # O vetor de entrada pode ter n valores
    n = len(vetor_entrada)

    # Um vetor de amostras com de tamanho k que inicializa com todos os valores em 0.
    # Este vetor armazenará as 'k' amostras mais recentes da entrada.
    vetor_amostras = np.zeros(k)

    # Um vetor de coeficientes do mesmo tamanho do vetor de amostras
    # com todos os valores iniciando em 1/k.
    vetor_coeficientes = np.full(k, 1/k)

    # Lista para armazenar o sinal de saída após a filtragem.
    vetor_saida = []

    print(f"Vetor de Coeficientes (tamanho {k}):\n{vetor_coeficientes}\n")

    # Itera sobre cada amostra do sinal de entrada.
    for i in range(n):
        # 1. Desloca os valores existentes no vetor de amostras uma posição para a direita.
        vetor_amostras = np.roll(vetor_amostras, 1)

        # 2. Carrega a nova entrada na primeira posição do vetor de amostras.
        vetor_amostras[0] = vetor_entrada[i]

        # 3. Calcula a saída do filtro.
        #    Multiplica cada amostra em 'vetor_amostras' pelo seu coeficiente
        #    correspondente e soma todos os resultados. Isso é a média.
        saida_filtro = np.sum(vetor_amostras * vetor_coeficientes)

        # 4. Armazena o resultado no vetor de saída.
        vetor_saida.append(saida_filtro)

        # Imprime o estado atual para fins de depuração e aprendizado.
        # print(f"Passo {i+1}: Entrada = {vetor_entrada[i]}")
        # print(f"  -> Vetor de Amostras: {np.round(vetor_amostras, 4)}")
        # print(f"  -> Saída do Filtro:   {round(saida_filtro, 4)}\n")


    return vetor_saida

# --- Exemplo de Uso com arquivo PCM ---

# Definição dos parâmetros do filtro
k_janela = 50    # Tamanho da janela do filtro (k)
pcm_file_path = '/content/sweep_20_3k4.pcm' # Substitua pelo caminho do seu arquivo .pcm

# Função para ler dados de um arquivo PCM
def read_pcm(file_path):
    """Reads 16-bit signed integer data from a raw PCM file."""
    data = []
    try:
        with open(file_path, 'rb') as f:
            while True:
                sample_bytes = f.read(2)  # Read 2 bytes for 16-bit audio
                if not sample_bytes:
                    break
                sample = struct.unpack('<h', sample_bytes)[0] # '<h' for little-endian signed short
                data.append(sample)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    return np.array(data)

# Leitura do arquivo PCM
sinal_entrada_pcm = read_pcm(pcm_file_path)

if sinal_entrada_pcm is not None:
    print("--- Iniciando Simulação do Filtro de Média Móvel com arquivo PCM ---")
    print(f"Sinal de Entrada lido do arquivo PCM (primeiras 10 amostras):\n{sinal_entrada_pcm[:10]}\n")

    # Chama a função para aplicar o filtro de média móvel no sinal.
    sinal_filtrado_pcm = media_movel(sinal_entrada_pcm, k_janela)

    print("--- Resultado Final ---")
    print(f"Sinal de Saída Filtrado (primeiras 10 amostras):\n{[round(x, 4) for x in sinal_filtrado_pcm[:10]]}")


    # --- Plotagem dos Sinais ---
    plt.figure(figsize=(12, 6))
    plt.style.use('seaborn-v0_8-whitegrid')

    # Plota o sinal de entrada do arquivo PCM
    plt.plot(sinal_entrada_pcm, label='Sinal de Entrada (PCM)')

    # Plota o sinal de saída (filtrado)
    plt.plot(sinal_filtrado_pcm, label=f'Sinal de Saída (Média Móvel, k={k_janela})')

    plt.title('Aplicação do Filtro de Média Móvel em Sinal PCM', fontsize=16)
    plt.xlabel('Amostra', fontsize=12)
    plt.ylabel('Amplitude', fontsize=12)
    plt.legend(fontsize=10)
    plt.show()
else:
    print("Não foi possível carregar o arquivo PCM.")
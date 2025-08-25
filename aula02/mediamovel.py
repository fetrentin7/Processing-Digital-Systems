import numpy as np
import matplotlib.pyplot as plt

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
        print(f"Passo {i+1}: Entrada = {vetor_entrada[i]}")
        print(f"  -> Vetor de Amostras: {np.round(vetor_amostras, 4)}")
        print(f"  -> Saída do Filtro:   {round(saida_filtro, 4)}\n")


    return vetor_saida

# --- Exemplo de Uso ---

# Definição dos parâmetros do filtro e do sinal
n_valores = 15  # Tamanho do vetor de entrada (n)
k_janela = 10    # Tamanho da janela do filtro (k)

# Geração do sinal de entrada: um impulso unitário.
# É um sinal que tem o valor 1.0 na primeira amostra e 0.0 nas demais.
sinal_impulso_unitario = np.zeros(n_valores)
sinal_impulso_unitario[0] = 1.0

print("--- Iniciando Simulação do Filtro de Média Móvel ---")
print(f"Sinal de Entrada (Impulso Unitário de {n_valores} amostras):\n{sinal_impulso_unitario}\n")

# Chama a função para aplicar o filtro de média móvel no sinal.
sinal_filtrado = media_movel(sinal_impulso_unitario, k_janela)

print("--- Resultado Final ---")
print(f"Sinal de Saída Filtrado:\n{[round(x, 4) for x in sinal_filtrado]}")


# --- Plotagem dos Sinais ---
plt.figure(figsize=(12, 6))
plt.style.use('seaborn-v0_8-whitegrid')

# Plota o sinal de entrada (impulso)
plt.stem(range(n_valores), sinal_impulso_unitario, linefmt='b-', markerfmt='bo', basefmt=' ', label='Sinal de Entrada (Impulso)')

# Plota o sinal de saída (filtrado)
plt.stem(range(n_valores), sinal_filtrado, linefmt='r-', markerfmt='ro', basefmt=' ', label=f'Sinal de Saída (Resposta ao Impulso, k={k_janela})')

plt.title('Resposta ao Impulso do Filtro de Média Móvel', fontsize=16)
plt.xlabel('Amostra (n)', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.xticks(range(n_valores))
plt.legend(fontsize=10)
plt.ylim(-0.1, 1.1)
plt.show()

NOME_ARQUIVO_PCM = "resposta_impulso.pcm"

print(f"\n--- Salvando o sinal de saída como dados PCM brutos em '{NOME_ARQUIVO_PCM}' ---")


sinal_escalado = np.array(sinal_filtrado) * 30000

# 2. Converter o sinal para o tipo de dados de inteiros de 16 bits (int16)
sinal_int16 = sinal_escalado.astype(np.int16)

# 3. Salvar os bytes brutos do array no arquivo .pcm, como solicitado
with open(NOME_ARQUIVO_PCM, 'wb') as f:
    f.write(sinal_int16.tobytes())






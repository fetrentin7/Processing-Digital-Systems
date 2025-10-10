import numpy as np
import matplotlib.pyplot as plt

def media_movel(vetor_entrada, k):

    if not isinstance(k, int) or k <= 0:
        raise ValueError("O tamanho da janela (k) deve ser um inteiro positivo.")

    # O vetor de entrada pode ter n valores
    n = len(vetor_entrada)

    vetor_amostras = np.zeros(k)
    vetor_saida = []
    vetor_coeficientes = np.full(k, 1/k)
    for i in range(n):
        vetor_amostras = np.roll(vetor_amostras, 1)
        vetor_amostras[0] = vetor_entrada[i]
        saida_filtro = np.sum(vetor_amostras * vetor_coeficientes)
        vetor_saida.append(saida_filtro)

    return vetor_saida


k_janela = 8
n_valores = 20 # Usaremos um número maior de amostras para ver melhor o efeito

sinal_impulso = np.zeros(n_valores)
sinal_impulso[0] = 1.0

sinal_degrau = np.ones(n_valores)

vetor_x_curto = [1, 0.5, 0.25, 0.125]
sinal_vetor_x = np.pad(vetor_x_curto, (0, n_valores - len(vetor_x_curto)), 'constant')


print(f"--- Simulação do Filtro de Média Móvel com k={k_janela} ---")

saida_impulso = media_movel(sinal_impulso, k_janela)
saida_degrau = media_movel(sinal_degrau, k_janela)
saida_vetor_x = media_movel(sinal_vetor_x, k_janela)

print("\n--- Resultados Finais ---")
print(f"Entrada (Impulso): \n{sinal_impulso}")
print(f"Saída (Impulso):   \n{[round(x, 4) for x in saida_impulso]}\n")

print(f"Entrada (Degrau): \n{sinal_degrau}")
print(f"Saída (Degrau):   \n{[round(x, 4) for x in saida_degrau]}\n")

print(f"Entrada (Vetor x): \n{sinal_vetor_x}")
print(f"Saída (Vetor x):   \n{[round(x, 4) for x in saida_vetor_x]}\n")



fig, axs = plt.subplots(3, 1, figsize=(12, 18), sharex=True)
plt.style.use('seaborn-v0_8-whitegrid')

# Gráfico 1: Resposta ao Impulso
axs[0].stem(range(n_valores), sinal_impulso, linefmt='b-', markerfmt='bo', basefmt=' ', label='Entrada (Impulso)')
axs[0].stem(range(n_valores), saida_impulso, linefmt='r-', markerfmt='ro', basefmt=' ', label=f'Saída (Resposta ao Impulso)')
axs[0].set_title(f'Resposta ao Impulso Unitário (k={k_janela})', fontsize=14)
axs[0].set_ylabel('Amplitude', fontsize=12)
axs[0].legend()
axs[0].grid(True)

# Gráfico 2: Resposta ao Degrau
axs[1].stem(range(n_valores), sinal_degrau, linefmt='b-', markerfmt='bo', basefmt=' ', label='Entrada (Degrau)')
axs[1].stem(range(n_valores), saida_degrau, linefmt='g-', markerfmt='go', basefmt=' ', label=f'Saída (Resposta ao Degrau)')
axs[1].set_title(f'Resposta ao Degrau Unitário (k={k_janela})', fontsize=14)
axs[1].set_ylabel('Amplitude', fontsize=12)
axs[1].legend()
axs[1].grid(True)

# Gráfico 3: Resposta ao Vetor x[n]
axs[2].stem(range(n_valores), sinal_vetor_x, linefmt='b-', markerfmt='bo', basefmt=' ', label='Entrada (Vetor x[n])')
axs[2].stem(range(n_valores), saida_vetor_x, linefmt='m-', markerfmt='mo', basefmt=' ', label=f'Saída (Resposta ao Vetor x[n])')
axs[2].set_title(f'Resposta ao Vetor x[n] (k={k_janela})', fontsize=14)
axs[2].set_xlabel('Amostra (n)', fontsize=12)
axs[2].set_ylabel('Amplitude', fontsize=12)
axs[2].legend()
axs[2].grid(True)

plt.xticks(range(n_valores))
plt.tight_layout()
plt.show()
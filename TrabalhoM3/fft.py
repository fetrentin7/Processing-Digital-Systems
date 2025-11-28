import numpy as np

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

    
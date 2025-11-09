# 1-a H(Z) = 1 + H0/2 * [1+ A(Z)]

# A(Z) = (Z^(-1) + aB) / (1 + aB * Z^(-1))
# Y(Z)/X(Z) = (Z^(-1) + aB) / (1 + aB * Z^(-1))
# Y1[n] = aB * X[n] + X[n-1] - aB * Y[n-1]

# Shelving LF para G=10dB e isso vai gerar um bo

# fc = 1000 Hz
# fs = 44100 Hz

# wc = 2 * pi * fc = 2 * pi * 1000 = 6283.185

# Y1[n] = aB * X[n] + X[n-1] - aB * Y[n-1]
# Y1[n] = 0.0086 * X[n] + X[n-1] - 0.0086 * Y[n-1]

# H(Z) = 1 + H0/2 * [1+ (Z^(-1) + aB) / (1 + aB * Z^(-1))]
# H(Z) = 1 + k * [1+ (Z^(-1) + aB) / (1 + aB * Z^(-1))]
# H(Z) = 1 + k * [[(1 + aB * Z^(-1))+ (Z^(-1) + aB)] / (1 + aB * Z^(-1))]
# H(Z) = 1 + [k(1 + aB) + [k * (aB + 1) * Z^(-1)] / (1 + aB * Z^(-1))
# H(Z) = [(1+aB*Z^(-1)) + k(1+aB) + k*(aB+1)*Z^(-1)] / (1+aB*Z^(-1))
# H(Z) = [k(1+aB) + (1+aB) + k*(aB+1)*Z^(-1)] / (1+aB*Z^(-1))

#sweep



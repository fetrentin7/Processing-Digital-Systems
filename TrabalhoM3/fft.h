
#ifndef FFT_H
#define FFT_H

#define PI 3.14159265358979323846
#define N 8

typedef struct {
    float re;
    float im;
} complex_t;

void fft_iterativa(complex_t* x, int N);

#endif

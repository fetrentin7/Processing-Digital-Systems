#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>

#define PI 3.14

typedef struct {
    double re;
    double im;
} complex_t;

complex_t add(complex_t a, complex_t b) {
    complex_t r;
    r.re = a.re + b.re;
    r.im = a.im + b.im;
    return r;
}

complex_t sub(complex_t a, complex_t b) {
    complex_t r;
    r.re = a.re - b.re;
    r.im = a.im - b.im;
    return r;
}

complex_t mul(complex_t a, complex_t b) {
    complex_t r;
    r.re = a.re * b.re - a.im * b.im;
    r.im = a.re * b.im + a.im * b.re;
    return r;
}
complex_t cis(double angle) {
    complex_t w;
    w.re = cos(angle);
    w.im = sin(angle);
    return w;
}

void fft(complex_t* x, int N) {

    if (N <= 1) return;

    int M = N / 2;

    complex_t* par = (complex_t*)malloc(M * sizeof(complex_t));
    complex_t* impar = (complex_t*)malloc(M * sizeof(complex_t));

    for (int i = 0; i < M; i++) {
        par[i] = x[2 * i];
        impar[i] = x[2 * i + 1];
    }

    fft(par, M);
    fft(impar, M);

    for (int k = 0; k < M; k++) {
        double angle = -2.0 * PI * k / N;

        complex_t Wk = cis(angle);
        complex_t t = mul(Wk, impar[k]);

        x[k] = add(par[k], t);
        x[k + M] = sub(par[k], t);
    }

    free(par);
    free(impar);
}

void fft_iterativa(complex_t* x, int N){

    int j = 0;
    for (int i = 1; i < N; i++) {
        int bit = N >> 1;
        while (j & bit) {
            j ^= bit; //se bit = 1, vira 0, se 0 vira 1
            bit >>= 1; //divide por 2
        }
        j |= bit; //liga o bit e  isso gera o próximo valor do índice reorganizado

        if (i < j) {
            complex_t temp = x[i];
            x[i] = x[j];
            x[j] = temp;
        }
    }

    for (int tam = 2; tam <= N; tam <<= 1) {

        double ang = -2.0 * PI / tam;
        complex_t w_m = cis(ang);

        for (int k = 0; k < N; k += tam) {

            complex_t w = { 1.0, 0.0 };

            for (int j = 0; j < tam / 2; j++) {

                complex_t t = mul(w, x[k + j + tam / 2]); 
                complex_t u = x[k + j];

                x[k + j] = add(u, t);
                x[k + j + tam / 2] = sub(u, t);

                w = mul(w, w_m);
            }
        }
    }
}

int main() {
    int N = 8;

    complex_t x[8];

    for (int n = 0; n < N; n++) {
        x[n].re = sin(2 * PI * 1 * n / N);
        x[n].im = 0.0;
    }

    //fft(x, N);
    fft_iterativa(x, N);

    for (int i = 0; i < N; i++) {
        printf("%d: %.5f + (%.5fj)\n", i, x[i].re, x[i].im);
    }

    return 0;
}
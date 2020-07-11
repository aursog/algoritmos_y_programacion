#include <stdio.h>

#define N 5

// Pasamos siempre los arreglos por referencia
int suma(int numeros[]) {
    int i = 0, sumaNumeros = 0;
    numeros[3] = 25;  // modifica el valor de la posición 3 del arreglo que está en main

    for (i = 0; i < N; i++) {
        sumaNumeros += numeros[i];
    }

    return sumaNumeros;
}

void printArreglo(int numeros[]) {
    int i;

    for (i = 0; i < N; i++) {
        printf("%d ", numeros[i]);
    }

    printf("\n");
}

int main() {
    int numeros[N] = {1, 2, 3, 4, 5};

    printArreglo(numeros);

    printf("La suma de los numeros es: %d\n", suma(numeros));

    printArreglo(numeros);
    return 0;
}
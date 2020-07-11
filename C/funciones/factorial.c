#include <stdio.h>

int factorial(int numero) {
    int i, resultado = 1;

    for (i = numero; i > 0; i--) {
        resultado = resultado * i;
    }

    return resultado;
}

int main() {
    int numero, resultado;

    printf("Ingrese un numero: ");
    scanf("%d", &numero);
    resultado = factorial(numero);
    printf("El factorial es: %d\n", resultado);
    return 0;
}
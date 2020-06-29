#include <stdio.h>

int main() {
    int variable1, variable2, resultado;

    printf("Ingrese variable 1: ");
    scanf("%d", &variable1);
    printf("Ingrese variable 2: ");
    scanf("%d", &variable2);

    resultado = variable1 + variable2;

    printf("La suma es: %d\n", resultado);
    return 0;
}
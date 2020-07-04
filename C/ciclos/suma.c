#include <stdio.h>

int main() {
    int numero, i = 0, resultado = 0;

    printf("Ingrese la cantidad de números a sumar: ");
    scanf("%d", &numero);

    do {
        resultado += i;
        i++;
    } while(i <= numero);

    printf("El resultado es: %d\n", resultado);
    return 0;
}
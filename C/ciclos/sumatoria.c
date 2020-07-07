#include <stdio.h>

int main() {
    int acumulador = 0, indice = 1;

    while(indice <= 100) {
        acumulador = acumulador + indice;
        indice++;
    }

    printf("%d\n", acumulador);

    return 0;
}
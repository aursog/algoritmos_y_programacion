#include <stdio.h>

int main() {
    // indices del arreglo, van del 0 hasta tamaño_arreglo - 1
    int arreglo[5], i;
    // asignación directa en la definición
    int otro_arreglo[5] = {2, 3, 4, 5, 6};

    // asignación cuadricula a cuadricula
    arreglo[0] = 1;
    arreglo[1] = 2;
    arreglo[2] = 3;
    arreglo[3] = 4;
    arreglo[4] = 5;

    for (i = 0; i < 5; i++) {
        printf("%d\n", arreglo[i]);
        printf("%d\n", otro_arreglo[i]);
    }

    return 0;
}
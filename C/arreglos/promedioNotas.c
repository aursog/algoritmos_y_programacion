#include <stdio.h>

int main() {
    int i;
    float promedio, notas[3];

    for (i = 0; i < 3; i++) {
        printf("Ingrese la nota %d ", i+1);
        scanf("%f", &notas[i]);
    }

    promedio = notas[0] * 0.3 + notas[1] * 0.35 + notas[2] * 0.35;
    printf("El promedio es %.2f\n", promedio);
    
    return 0;
}
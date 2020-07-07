#include <stdio.h>

int main() {
    int numero1, numero2, opc;
    float resultado;

    printf("Seleccione una de las siguientes opciones\n");
    printf("\t 1.- Sumar \n");
    printf("\t 2.- Restar \n");
    printf("\t 3.- Multiplicar \n");
    printf("\t 4.- Dividir \n");
    scanf("%d", &opc);

    printf("\n\nIngrese el numero 1: ");
    scanf("%d", &numero1);

    printf("\nIngrese numero 2: ");
    scanf("%d", &numero2);

    switch(opc) {
        case 1:
            resultado = numero1 + numero2; // 12
            break;
        case 2:
            resultado = numero1 - numero2; // 8
            break;
        case 3:
            resultado = numero1 * numero2;
            break;
        case 4:
            resultado = (float) numero1 / (float) numero2;
            break;
        default:
            printf("Opcion ingresa es inválida\n");
            resultado = -1;
            break;
    }

    printf("\n\nEl resultado es: %.2f\n", resultado);
    return 0;
}
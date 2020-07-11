#include <stdio.h>

// Paso de parámetro por valor
int suma2(int a, int b) {
    b = 500; // no me modifica el valor de la variable numero
    return a + b;
}

// Paso de parámetro por referencia
int suma(int a , int *b) {
    int c = 5;
    *b = 2; // modifico el valor de la variable numero
    return a + *b + c;
}

int main() {
    int numero;
    printf("Ingrese un numero ");
    scanf("%d", &numero);

    printf("%d\n", numero);
    printf("%d\n", suma2(3, numero));
    printf("%d\n", numero);
    printf("%d\n", suma(3,&numero)); // suma(3, 5)
    printf("%d\n", numero);
    return 0;
}
#include <stdio.h>
#include <stdlib.h>

// Esto se define en tiempo de compilación
#define N 5

int main() {
    int tamano = 10, largo; // define en tiempo de ejecución
    int otro_arreglo[tamano]; // eventualmente correcto -- pero puede generar errores
    int nuevo_arreglo[largo]; // Incorrecto -- puede que funciones, pero les va a generar
                             // errores dependiendo del S.O.
    int tamanioOtro, tamanioNuevo;
    int arreglo[N]; // correcto ==> arreglo[5]

    scanf("%d", &largo);
    tamanioOtro = sizeof(otro_arreglo) / sizeof(int);
    tamanioNuevo = sizeof(nuevo_arreglo) / sizeof(int);

    printf("Tamaño arreglo otro_arreglo: %d\n", tamanioOtro);
    printf("Tamaño arreglo nuevo_arreglo: %d\n", tamanioNuevo);
    
    return 0;
}
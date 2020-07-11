#include <stdio.h>
#include <string.h>

struct alumno {
    int edad;
    float notas[3];
    char nombre[50];
};

int main() {
    struct alumno a1;
    a1.edad = 13;
    a1.notas[0] = 3.5;
    a1.notas[1] = 4;
    a1.notas[2] = 20;
    strcpy(a1.nombre, "Pepe");

    printf("%d\n", a1.edad);
    printf("%.2f\n", a1.notas[0]);
    printf("%.2f\n", a1.notas[1]);
    printf("%.2f\n", a1.notas[2]);
    printf("%s", a1.nombre);
}
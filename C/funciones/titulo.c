#include <stdio.h>

// Tiene que estar definida antes que la función título
void otroTitulo() {
    printf("Este es otro título\n");
}

// Tiene que estar definida antes que la función main
void titulo() {
    printf("Este es un título\n");
    otroTitulo();
}

int main() {
    titulo();
    return 0;
}
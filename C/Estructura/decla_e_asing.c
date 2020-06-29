#include <stdio.h>

int main() {
    int i, j, k = 0, z, y = 1; // declarando y asignando valores
    
    x = 20; // Error, x no está declarada
    i = j + y; // acá j no está asignada, el compilador le asigna 0 o MAX_INT
               // o a un número random del sistema
    
    printf("%d", i);
    return 0;
}
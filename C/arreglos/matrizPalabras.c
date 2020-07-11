#include <stdio.h>

int main() {
    int i, j;
    char frutas[4][7] = {"banana", "pera", "manzana", "uva"};

    for (i = 0; i < 4; i++) {
        for (j = 0; j < 7; j++) {
            printf("%c", frutas[i][j]);
        }
        printf("\n");
    } 

    return 0;
}
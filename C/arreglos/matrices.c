#include <stdio.h>

int main() {
    int matriz[4][3];
    // a través de definicion
    int superMatriz[3][3] = {{3,1,5}, {3,6,7}, {10, 100, 1000}};
    int i, j;

    // Elemento a elemento
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 3; j++) {
            matriz[i][j] = 1;
        }
    }
    return 0;
}
#include <stdio.h>

int main() {
    int matriz[3][2] = {{0,1},{3,2},{4,5}};

    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 2; j++) {
            printf("%d", matriz[i][j]);
        }

        printf("\n");
    }

    return 0;
}
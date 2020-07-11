#include <stdio.h>

int main() {
    int i = 0;

    printf("NUMEROS PARES\n");
    while (i <= 10) {
        if (i % 2 == 0) {
            printf("%d\n", i);
        }

        i++;
    }

    printf("NUMEROS IMPARES\n");

    for (i = 0; i <= 10; i++) {
        if (i % 2 != 0) {
            printf("%d\n", i);
        }
    }
    
    return 0;    
}
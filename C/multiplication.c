//
// Created by Anggelo Marccelo Urso Goddard on 2/17/20.
//

#include <stdio.h>

int main() {
    int mult, result = 0, sum, i;

    printf("Ingrese multiplicando:\n");
    scanf("%d", &mult);

    printf("Ingrese multiplicador:\n");
    scanf("%d", &sum);

    for (i = 0; i < sum; i++) {
        result += mult;
    }

    printf("El resultado de %d * %d = %d\n", mult, sum, result);

    return 0;
}
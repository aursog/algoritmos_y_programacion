#include <stdio.h>
#include <string.h>

int main() {
    int i;
    char palabra[6] = {'b','a','n','a', 'n', 'a'};

    // mostrando caracter a caracter
    for (i = 0; i < 6; i++) {
        printf("%c", palabra[i]);
    }

    // lo muestro como string
    printf("%s\n", palabra);
    return 0;
}
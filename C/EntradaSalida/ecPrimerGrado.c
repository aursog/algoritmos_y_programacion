#include <stdio.h>

int main() {
    int a, b;
    float x; 

    scanf("%d", &a);
    scanf("%d", &b);

    if (a == 0) {
        if (b == 0) {
            printf("La ecuación tiene infinitas soluciones\n");
        } else {
            printf("La ecuación tiene no tiene solución\n");
        }
    } else {
        x = -b / a;
        printf("%d", x);
    }
    
    return 0;
}
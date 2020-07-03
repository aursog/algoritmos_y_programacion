#include <stdio.h>

int main() {
    int i;
    
    scanf("%d", &i);

    if (i < 10) 
        printf("El número %d es menor que 10\n", i);
    else
        printf("El número %d es mayor que 10\n", i);
        

    return 0;
}
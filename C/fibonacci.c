#include <stdio.h>

int main() {
	int fib1=0, fib2=1, hasta, i;

	printf("Ingrese hasta\n");
	scanf("%d", &hasta);

	for ( i = 0; i < hasta; i++) {
		fib2 = fib2 + fib1;
		fib1 = fib2 - fib1;
		printf("%d\n", fib1);
	}

	return 0;
}

#include<stdio.h>

int main() {
	char c = 'c';
	char b = 'b';
	char ab;

	ab = c + b;

	printf("%s\n", &ab);
	
	return 0;
}

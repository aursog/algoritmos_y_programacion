Algoritmo suma_gauss
	definir acumulador, indice Como Entero;
	
	acumulador = 0;
	indice = 1;
	
	mientras indice <= 100 Hacer
		acumulador = acumulador + indice;
		indice = indice + 1;
	FinMientras
	
	mostrar acumulador;
FinAlgoritmo

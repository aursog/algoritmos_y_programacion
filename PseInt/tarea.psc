Algoritmo tareaPotencia2
	definir n Como Entero
	definir resultado Como Entero
	
	n = 0
	
	// con instruccion mientras
	mientras n <= 10 hacer
		resultado = 2^n
		mostrar "2 elevado a " n " es: " resultado
		n = n + 1
	FinMientras
	
	// con instruccion para hasta
	para n = 0 hasta 10 con paso 1 Hacer
		resultado = 2^n
		mostrar "2 elevado a " n " es: " resultado
	FinPara
	
FinAlgoritmo

Algoritmo potencia
	definir base Como Entero
	definir exponente Como Entero
	definir resultado Como Entero
	
	leer base
	leer exponente
	
	resultado = 1
	
	mientras exponente != 0 Hacer
		resultado = base * resultado
		exponente = exponente - 1
	FinMientras
	
	mostrar resultado
	
FinAlgoritmo

Algoritmo potencia
	definir base Como Entero
	definir exponente Como Entero
	definir indice Como Entero
	definir resultado Como Entero
	
	leer base
	leer exponente
	
	si exponente == 0 Entonces
		mostrar 1
	sino
		si exponente == 1 entonces
			mostrar base
		sino
			indice = 2
			resultado = base * base
			
			mientras indice != exponente Hacer
				resultado = base * resultado
				indice = indice + 1
			FinMientras
			
			Mostrar resultado
		FinSi
	FinSi
	
FinAlgoritmo

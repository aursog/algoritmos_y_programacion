Algoritmo potencia
	base Es Entero
	exponente Es Entero
	resultado es entero
	
	resultado <- 1
	leer base
	leer exponente
	
	si base < 0 entonces 
		mostrar "la base tiene que ser positiva"
	sino 
		mientras exponente != 0 hacer
			resultado = resultado * base
			exponente <- exponente - 1
		FinMientras
		
		mostrar resultado
	FinSi
	
FinAlgoritmo

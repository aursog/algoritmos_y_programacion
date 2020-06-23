Algoritmo actividad1
	Definir cantidad Como Entero
	cantidad <- 0

	Mientras cantidad<=10 Hacer
		Escribir 'El resultado es: ',potencia(2,cantidad)
		cantidad <- cantidad+1
	FinMientras
FinAlgoritmo

Funcion resultado <- potencia(base,exponente)
	resultado <- 1
	Mientras exponente!=0 Hacer
		resultado <- resultado*base
		exponente <- exponente-1
	FinMientras
FinFuncion

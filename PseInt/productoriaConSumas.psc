Algoritmo multi_gauss
	Definir acumulador, indice como Entero
	Definir secundario, segAcumulador Como Entero
	
	acumulador = 1
	indice = 1
	
	mientras indice <= 10 Hacer
		acumulador = miMultiplicacion(indice, acumulador)
		indice = indice + 1
	FinMientras
	
	mostrar acumulador
	
FinAlgoritmo


funcion segAcumulador <- miMultiplicacion(multiplicando, multiplicador)
	Definir secundario, segAcumulador como Entero
	secundario = 1
	segAcumulador = 0

	mientras secundario <= multiplicador Hacer
		segAcumulador = segAcumulador + multiplicando
		secundario = secundario + 1
	FinMientras
FinFuncion
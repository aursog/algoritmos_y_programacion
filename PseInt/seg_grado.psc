Algoritmo seg_grado
	Definir a,b,c,discriminante Como Entero
	Definir x1,x2 Como Real
	Leer a
	Leer b
	Leer c
	Si a==0 Entonces
		Si b==0 Entonces
			Si c==0 Entonces
				Escribir 'La ecuación tiene infinitas soluciones'
			SiNo
				Escribir 'La ecuación no tiene solución'
			FinSi
		SiNo
			x_1 <- -c/b
			Escribir resultado
		FinSi
	SiNo
		discriminante <- b^2-4*a*c
		Si discriminante<0 Entonces
			Escribir 'La ecuación no tiene soluciones reales'
		SiNo
			x_1 <- (-b+raiz(discriminante))/2*a
			x_2 <- (-b-raiz(discriminante))/2*a
			Escribir 'los valores son: ',x_1,x_2
		FinSi
	FinSi
	
	Segun n Hacer
		Opcion 1:
			mostrar "lala"
		Opcion 2:
			mostrar "lolo"
		Opcion 3:
			mostrar "lele"
	FinSegun
FinAlgoritmo

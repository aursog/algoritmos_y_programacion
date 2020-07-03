Algoritmo seg_grado
	Definir a, b, c, discriminante Como Entero;
	definir x1, x2 Como Real;
	
	Leer a;
	Leer b;
	Leer c;
	
	si a == 0 Entonces
		si b == 0 Entonces
			si c == 0 Entonces
				mostrar "La ecuación tiene infinitas soluciones";
			SiNo
				mostrar "La ecuación no tiene solución";
			FinSi
		SiNo
			x_1 = -c / b;
			mostrar resultado;
		FinSi
	SiNo
		discriminante = b^2 - 4*a*c
		si discriminante < 0 Entonces
			mostrar "La ecuación no tiene soluciones reales"
		sino
			x_1 = (-b + raiz(discriminante)) / 2*a
			x_2 = (-b - raiz(discriminante)) / 2*a
			mostrar "los valores son: ", x_1, x_2;
		FinSi
	FinSi
FinAlgoritmo

Algoritmo ec_primer_grado
	Definir a,b Como Entero;
	Definir x Como Real;
	
	// Paso 1
	Leer a;
	Leer b;
	
	// Validación del paso 2
	Si a == 0 Entonces
		// validación del paso 3
		si b == 0 Entonces
			// Mostrar del paso 3
			mostrar "La ecuación tiene infinitas soluciones";
		sino
			// Mostrar en el paso 4
			mostrar "La ecuación no tiene solución";
		FinSi
	SiNo
		// paso 5
		x = -b / a;
		mostrar "El resultado es: ", x;
	FinSi
// Paso 7
FinAlgoritmo

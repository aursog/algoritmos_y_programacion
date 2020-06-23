Algoritmo calculadora_basica
	numero_uno Es Entero
	numero_dos Es Entero
	resultado Es real
	
	leer numero_uno
	leer numero_dos
	
	resultado <- numero_uno + numero_dos
	mostrar "La suma es: " resultado
	
	resultado <- numero_uno - numero_dos
	mostrar "La resta es: " resultado
	
	resultado <- numero_uno * numero_dos
	mostrar "la multiplicacion es: " resultado
	
	si numero_dos == 0 Entonces
		mostrar "Error, division por 0 no existe"
	SiNo
		resultado <- numero_uno / numero_dos
		mostrar "La division es: " resultado
	FinSi
 	
FinAlgoritmo

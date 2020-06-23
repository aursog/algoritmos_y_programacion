import math 

a = int(input("Ingrese el lado a: "))
b = int(input("Ingrese el lado b: "))
c = int(input("Ingrese el lado c: "))

# calculamos s
s = (a + b + c) / 2

# calculamos el área
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# calculamos el perímetro
perimetro = a + b + c 

# mostramos resultados por pantalla
print(f"El área es {area}")
print(f"El perímetro es {perimetro}")
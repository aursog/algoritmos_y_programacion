import math

a = int(input("Ingrese lado a: "))
b = int(input("Ingrese lado b: "))
angulo = int(input("Ingrese el ángulo (en grados): "))

# transformamos el ángulo de grados a radianes
radianes = angulo * math.pi / 180

area = 1 / 2 * a * b * math.sin(radianes)
print(f"El area es {area}")
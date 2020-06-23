base = int(input("Ingrese base: "))
exponente = int(input("Ingrese exponente: "))

i = 0
resultado = 1
while i < exponente:
    resultado *= base
    i += 1

print(resultado)
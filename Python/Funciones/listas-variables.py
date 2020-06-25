def modifica(a,b):
    a.append(4)
    b = b + [4]
    return b

lista1 = [1,2,3]
lista2 = [1,2,3]
lista3 = modifica(lista1, lista2)

print(lista1)
print(lista2)
print(lista3)
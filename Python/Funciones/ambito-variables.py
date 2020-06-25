def modifica(a, b):
    a[0] = 5 
    b = b + [4]
    return b

lista1 = [1,2,3]
lista2 = [1,2,3]
lista3 = modifica(lista1, lista2)

print(lista1) # [1,2,3,4]
print(lista2) # [1,2,3]
print(lista3) # [1,2,3,4]
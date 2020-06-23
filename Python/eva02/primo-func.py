def divisores(numero):
    es_primo = True
    
    for dividendo in range(2,numero):
        resto = numero % dividendo

        if resto == 0:
            es_primo = False
            break
    
    return es_primo

# Flujo principal
for numero in range(2, 101):
    if (divisores(numero)):
        print(f"El numero {numero} es primo")
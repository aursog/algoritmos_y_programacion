numeroBandas = int(input("Ingrese numero de bandas: "))
colores = []

tabla = {
    "negro": {
        "valor": 0,
        "multiplicador": 1,
        "tolerancia": 0,
        "coefTemp": 0
    },
    "marron": {
        "valor": 1,
        "multiplicador": 10,
        "tolerancia": -1,
        "coefTemp": 100
    },
    "rojo": {
        "valor": 2,
        "multiplicador": 100,
        "tolerancia": -2,
        "coefTemp": 50
    },
    "naranja": {
        "valor": 3,
        "multiplicador": 1000,
        "tolerancia": -3,
        "coefTemp": 15
    }
}

for _ in range(numeroBandas):
    color = input(f"Ingrese color banda {_+1} ")
    colores.append(color)

valorOn = ""

for color in colores:
    valorOn = str(tabla[color]["valor"]) + valorOn

print(valorOn)
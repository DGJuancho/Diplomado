"""Crear un programa que reciba una sucesión de 0s y 1s y luego determine si la cantidad 0s y 1s es par o impar."""

sucesion = input("Por favor ingrese una secuencia de 0s y 1s: ")

contar_0 = sucesion.count("0")
contar_1 = sucesion.count("1")

if contar_0 % 2 == 0:
    print("La cantidad de 0s es par")
else:
    print("La cantidad de 0s es impar")

if contar_1 % 2 == 0:
    print("La cantidad de 1s es par")
else:
    print("La cantidad de 1s es impar")

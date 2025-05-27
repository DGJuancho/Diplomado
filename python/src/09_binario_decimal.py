"""Realizar un programa en el cual el usuario luego de ingresar un número
en sistema binario, se le muestre el mismo en sistema decimal."""

# CALCULADORA DE BINARIO A DECIMAL

binario = [input("Por favor ingrese un número binario: ")]

binario.reverse()

i = 0
decimal = 0
while i < len(binario):
    elemento = int(binario[i]) * (2**i)
    decimal = decimal + elemento
    i = i + 1


print(f"El número ingresado, convertido en el sistema decimal es: {decimal}")

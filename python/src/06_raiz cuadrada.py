"""Realice un programa que pida al usuario un número real (flotante) para luego imprimir su raíz cuadrada. Si el resultado tiene decimales, limite la cantidad de los mismos a 2."""

import math

numero = float(input("Por favor ingrese un número real: "))

raiz_cuadrada = math.sqrt(numero)

print(f"La raiz cuadrada de {numero} es: {raiz_cuadrada:.2f}")

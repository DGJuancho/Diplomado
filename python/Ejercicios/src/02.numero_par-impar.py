"""
Crear un programa que detecte si un número entero ingresado por el usuario es par o impar.
"""

numero = int(input("Introduzca un número entero: "))

resultado = "PAR" if numero % 2 == 0 else "IMPAR"

print(f"El número {numero} es: {resultado}")

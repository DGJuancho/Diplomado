"""Elabore un programa que le pida al usuario 4 números reales (use float() ) y luego el programa debe imprimir el promedio de ellos."""

num1 = float(input("Por favor indique el primer número: "))
num2 = float(input("Por favor indique el segundo número: "))
num3 = float(input("Por favor indique el tercer número: "))
num4 = float(input("Por favor indique el cuarto número: "))

numeros = [num1, num2, num3, num4]

promedio = sum(numeros) / len(numeros)

print(f"El promedio de los {len(numeros)} números es de: {promedio}")

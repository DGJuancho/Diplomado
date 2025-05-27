"""Elaborar un programa que le pida un número entero n, luego pida n veces al usuario que ingrese texto (por ejemplo un nombre), luego de terminar de pedir esos datos, imprima los datos recogidos pero en el orden inverso a como se recibieron."""

n = int(input("Por favor ingrese un número entero: "))
i = 0
nombres = []

while i < n:
    nombres.append(input("Por favor ingrese un nombre: "))
    i = i + 1

nombres.reverse()
for nombre in nombres:
    print(nombre)

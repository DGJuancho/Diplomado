"""Realice un programa que le pida una cadena de caracteres (cualquier cosa) al usuario y que después muestre lo que ingresó el usuario pero al revés."""

cadena = input("por favor ingrese una cadena de caracteres: ")

i = len(cadena) - 1
nva_cadena = ""
while i >= 0:
    nva_cadena = nva_cadena + cadena[i]
    i = i - 1
print(f'Lo  que usted ingresó "{cadena}" visto al revés es: {nva_cadena}')

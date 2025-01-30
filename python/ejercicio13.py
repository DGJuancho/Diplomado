"""Dada una lista de 5 palabras dadas por el usuario, crea otra lista que contenga sólo aquellas palabras que tengan más de 3 consonantes. Imprime la nueva lista."""

palabras = input("Por favor ingrese 5 palabras: ")

lista = palabras.split()
nva_lista = []

for palabra in lista:
    vocales = 0
    for vocal in palabra:
        if vocal in ("aeiou"):
            vocales += 1
    if (len(palabra) - vocales) > 3:
        nva_lista.append(palabra)

print(nva_lista)

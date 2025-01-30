"""Dada una lista de 5 palabras dadas por el usuario, crea otra lista que contenga sólo aquellas palabras que tienen más de 5 letras. Imprime la nueva lista."""

palabras = input("Por favor ingrese 5 palabras: ")

lista = palabras.split()
nva_lista = []

for palabra in lista:
    if len(palabra) > 4:
        nva_lista.append(palabra)
print(f"De las 5 palabras ingresadas, sólo estas tienen 5 o más letras: {nva_lista}")

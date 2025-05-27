"""Dado un diccionario de nombres y direcciones (créelo en el código, al menos 5 pares), encuentra la dirección de una persona específica utilizando la clave correspondiente. Pide al usuario que ingrese el nombre y luego imprime la dirección"""

datos = {
    "Juancho": "La Vaquera",
    "María": "La Candelaria",
    "Juanvi": "Las CLavellinas",
    "Luis": "Trapichito",
    "Valeria": "Menca",
}

nombre = input("Por favor ingrese el nombre que desea buscar: ")

print(f"{nombre} vive en: {datos[nombre]}")

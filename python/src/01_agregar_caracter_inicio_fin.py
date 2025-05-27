"""Crear un programa que le pida al usuario cualquier palabra, secuencia de números u oración para que luego el programa imprima lo mismo pero con una “a” al principio y una “a” al final."""

mensaje_usuario = input(
    "Por favor ingrese una secuencia de caracteres, pueden ser palabras, números, frases, lo que desee: "
)

print("a" + mensaje_usuario + "a")

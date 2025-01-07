"""Hacer un programa que reciba una string (cadena de caracteres) y detecte si es palindromo. (que se pueda leer igual de izquierda a derecha y viceversa).
"""

palabra = input("Ingrese una palabra: ")
palabra_minus = palabra.lower()
palindromo = palabra_minus[::-1]

if palabra_minus == palindromo:
    print(f'La palabra "{palabra}" es palindromo')

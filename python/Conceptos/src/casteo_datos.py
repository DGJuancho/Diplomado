"""
Comúnmente llamado casting, este proceso consiste en convertir un tipo de dato a otro. Podemos hacer que un número con decimales, pase a ser un número entero, o un string lleno de números se pueda operar matemáticamente. Este proceso puede ser llevado a cabo con las funciones int(), float(), str(). Estas son las funciones de conversión de tipo de dato.
Por ejemplo:
int () # convierte a entero
str(c) # convierte a string
float() # convierte a flotante
"""

a = 18.1039
a = int(a)
print(a)
print(float(a))
b = "340"
b = int(b)
b = b + a
print(b)
c = 34
c = str(c)
print(c + " texto")

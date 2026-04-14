"""
Las librerías también llamadas módulos consisten en un repertorio de funciones diseñadas que para realizar tareas específicas y que podemos tomar prestadas. Para añadir un módulo a nuestro código usamos la palabra reservada import y luego el nombre del mismo. Al importar un módulo podemos utilizar un "alias" para el mismo de forma que podamos utilizar de forma abreviada en el código.

Como ejemplo tenemos al módulo math que contiene una gran variedad de funciones vinculadas al mundo de la matemática. Para usar una función de un módulo importado debemos escribir el nombre del módulo, seguidamente de un punto y luego el nombre de la función. En el ejemplo utilizamos la letra m como alias del módulo math.

Es posible que de un módulo tomemos prestado sólo las funciones que queramos usar. Eso hará que nuestro código sea más eficiente. Esto es posible usando la palabra clave from. en el ejemplo importamos sólo la función randint del módulo random.
"""

import math as m
from random import randint

a = int(m.log2(64))
print(f"logaritmo de base 2 de 64 = {a}")
b = int(m.cos(0))
print(f"coseno de 0 = {b}")
c = int(m.fabs(-50))
print(f"valor absoluto de -50 es: {c}")
d = m.sqrt(625)
print(f"La raíz cuadrada de 625 es: {d}")

# A contendrá un número pseudo aleatorio entero entre 1 y 100
A = randint(1, 100)
print(
    f"{A}, es un número entero pseudoaleatorio generado por la función randint importada del módulo random.",
    end=" ",
)

e = "El seno de 45 Grados es: "
print(e, m.sin(m.radians(45)))

"""
Los condicionales conforman un grupo de sentencias que permiten que nuestros programas tomen decisiones en función de una condición propuesta. Los condicionales están presente en todos los lenguajes de programación de propósito general.

La sentencia principal de todo condicional es if . La sentencia condicional if ejecutará las instrucciones que estén dentro de ella, sólo si se cumple una condición planteada por nosotros.
"""

a = int(input())
if a > 5:
    b = 9
    print(b + 1)
print(2)

if 2 + 2 == 5:
    print(1)
else:
    print(2)

a = int(input())
if a >= 42:
    print(1)
elif a >= 29:
    print(2)
elif a >= 0:
    print(3)
else:
    print(4)

a = int(input())
if a >= 42:
    b = int(input())
    if b == 5:
        print(1)
        print(2)
    elif b == 2:
        print(3)
    else:
        print(6)
else:
    print(5)

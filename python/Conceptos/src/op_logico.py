"""
Operadores Lógicos
En Python tenemos, los siguientes operadores lógicos:

Operadores lógicos comparación: > , <, >=, <=, ==

Operadores lógicos de agrupación: and or

Operador lógico de negación: not

Estos operadores, se usan para trabajar expresiones lógicas. El resultado de utilizarlos en alguna operación lógica es siempre True o False (verdadero o falso)
"""

a = 3 > 800
b = 14 >= 7
c = 5 == 5
d = not c
print(a, b, c, d)

a = 59 <= 1
b = 45 > 1381
c = 33 == 33
d = a or b
e = b or c
f = c and e
g = not d
print(d, e, f, g)

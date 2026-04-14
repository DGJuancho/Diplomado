"""
Operadores Matemáticos
En Python trabajaremos con los siguientes operadores matemáticos: “+” (suma), “-” (resta), “*” (multiplicación), “/” (división), “//” (división entera), “%” (módulo) “**” (potenciación).
"""

# suma y resta

a = 7
b = 12.5

print(a + b)

# Multiplicación

c = a * b

print(c * 2)

# División normal
x = 4
d = 2
z = x / d
print(f"El valor de z es: {z}")

# División entera
t = 5
d = 7
z = d // t
print(f"El valor de z es: {z}")

# Modulo
x = 16 % 2
print(x)
a = 3
x = 8 % a
print(x)

# Potenciación
a = 2**4
print(a)

# Asi puedes calcular las raíz cuadrada
b = 4 ** (1 / 2)
print(b)

# Asi puedes calcular la raíz cúbica
c = 125 ** (1 / 3)
print(c)

# concatenación de strings
a = "Hola "
b = "¿cómo estás?"
print(a + b)

# se imprime ese string junto tantas veces se desee
c = "abc "
print(c * 3)

d = 200
d += 10
print(d)  # es como escribir d = d+10

d -= 20
print(d)  # es como escribir d=d-20

f = 4
f *= 4
print(f)  # es como escribir f = f*4

f //= 4
print(f)  # es como escribir f = f//4

f **= 2
print(f)  # es como escribir f = f**2

f %= 2
print(f)  # es como escribir f = f%2

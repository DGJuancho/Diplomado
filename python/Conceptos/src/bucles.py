"""Los ciclos, también llamados bucles conforman al igual que los condicionales estructuras que están presentes en todos los lenguajes de propósito general. Los ciclos son estructuras iterativas que van a ejecutar

una o varias instrucciones tantas veces nosotros queramos mientras se cumpla una condición.
"""

# Bucle While

i = 1
while i <= 10:
    print(i, end=" ")  # Define el carácter final de la impresión.
    i += 1
print()


# Bucle for
for n in range(10, 0, -1):
    print(n, end=" ")
print()

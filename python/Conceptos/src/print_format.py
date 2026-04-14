"""
Formatear la salida de la función print
Existe varias maneras de realizar una impresión en python, esto es gracias a que la función print tiene varios trucos.
"""

# Forma 1: Usando strings, comas y colocando las variables en las posiciones deseadas dentro de la función print( )

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
print("Su nombre es: ", nombre, "y su edad es: ", edad)

# Forma 2: utilizando la función str() y aplicando la operación suma.

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
print("Su nombre es: " + str(nombre) + " y su edad es: " + str(edad))

# Forma 3: utilizando la función format (), Desde la versión 3.6 de python esta forma imprimir se simplificó. Se coloca una f antes del string y dentro de llaves se colocan las variables que se desea que aparezcan en esa parte del string.

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
print(f"Su nombre es: {nombre} y su edad es: {edad}")

"""Forma 4: utilizando %d para variables enteras

%s para los strings

%f para flotantes

Estos se colocan dentro del string que se desea imprimir, luego después de éste se coloca porcentaje y luego las variables en el orden en que se colocaron los modificadores de formato respectivos a su tipo de dato."""

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
print("Su nombre es: %s y su edad es: %d" % (nombre, edad))

"""Con el modificador de formato %f que trabaja con flotantes, podemos limitar la cantidad de decimales que se mostrará en la impresión de un número con decimales. Por defecto, con este modificador se mostrará 6 decimales y los que falte los completará con 0."""

# Por defecto el modificador muestra 6 dígitos decimales
a = 58.17274491
print("%f" % a)

# Para modificarlo se coloca el número de dígitos decimales luego del símbolo de porcentaje
a = 58.17274491
print("%.3f" % a)

"""Por defecto luego de terminar su trabajo, la función print() produce un salto de línea, esto hace que la próxima impresión aparezca debajo de la anterior.

Podemos hacer que varias impresiones aparezcan en la misma línea colocando de último como argumento end=' ' esto hará que la próxima impresión aparezca luego de un espacio."""

a = 5
print(a, end=" ")
b = 41.71
print(b, end=" ")
c = 7
print(c)

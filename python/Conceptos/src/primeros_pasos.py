"""
Tenemos varios tipos de datos primarios, tales como:
string, cadena de texto, son caracteres encerrados entre comillas simples o dobles.
int, (enteros) son números enteros positivos y negativos
float, (decimales), son números que tienen una parte decimal, también pueden ser positivos o negativos.
bool (Booleano) este tipo de dato tiene dos valores True o False, se utilizan sobretodo en expresiones condicionales y bucles.
"""

# función print, se usa mostrar una salida en la consola.

print("Hello, world!")
a = 5
b = 45.5
print(a, b)

c = True
d = False

print(f'El valor de c es: "{c}" y la variable d es: "{d}"')

e = input("Por favor introduzca un valor: ")
f = int(input("Por favor introduzca un valor entero: "))
g = float(input("Por favor introduzca un valor deimal: "))

print(f'Usted ingreso "{e}", luego "{f}" y finalmente "{g}"')

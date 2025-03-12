"""Crear una calculadora de operaciones aritméticas, el usuario debe ingresar dos números y debe elegir cuál operación efectuar para que luego se muestra en la salida el resultado. La interfaz se deja a su elección al igual que el orden de los datos de entrada."""

print("CALCULADORA ARITMÉTICA")
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Denominador Inválido"


def potencia(a, b):
    return a**b


def salir():
    print("Saliendo del programa...")
    exit()


while True:
    print("-ELIJA UNA OPCIÓN-")
    print("1) Para sumar")
    print("2) Para restar")
    print("3) Para multiplicar")
    print("4) Para dividir")
    print("5) Para potencia")
    print("6) Para salir")
    opcion = int(input())

    operaciones = {
        1: suma,
        2: resta,
        3: multiplicacion,
        4: division,
        5: potencia,
        6: salir,
    }

    if operaciones[opcion] == salir:
        salir()

    elif opcion in operaciones:

        resultado = operaciones[opcion](a, b)
        print(f"El resultados de la operación es: {resultado}")
        print("-------------------------------")
        print("\n")
        print("¿Desea realizar otra operación? (s/n)")
        respuesta = input()
        if respuesta == "n":
            salir()
        elif respuesta == "s":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
    else:
        print("Opción inválida, por favor elija una opción válida")

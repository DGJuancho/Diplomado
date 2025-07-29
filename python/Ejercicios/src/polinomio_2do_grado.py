import math  # Función necesaria para calcular las raíces cuadradas

"""Realice un programa en Python que halle (y notifique si no es posible) las raíces de un polinomio de segundo grado. El usuario pasará los coeficientes del polinomio.
Recuerde que un polinomio de 2do grado tiene la siguiente forma: ax2+bx+c=0 y los coeficientes son números reales (use float) son a,b y c."""

print("--- Calculadora de Raíces para Polinomios de Segundo Grado ---")

# 1.- Pedir los coeficientes al usuario
coeficiente_a = float(input("Ingrese el coeficiente 'a': "))
coeficiente_b = float(input("Ingrese el coeficiente 'b': "))
coeficiente_c = float(input("Ingrese el coeficiente 'c': "))

# 2.- Verificar si a = 0
if coeficiente_a == 0:
    print(
        "\nError: El coeficiente 'a' es igual a 0, por tanto la ecuación no es un polinomio de 2do. Grado"
    )

else:
    # 3.- Evaluar el discriminante
    discriminante = (coeficiente_b**2) - (4 * coeficiente_a * coeficiente_c)

    if discriminante > 0:
        raiz1 = (-coeficiente_b + math.sqrt(discriminante)) / (2 * coeficiente_a)
        raiz2 = (-coeficiente_b - math.sqrt(discriminante)) / (2 * coeficiente_a)
        print("\nEl polinomio tiene dos raíces reales diferentes:")
        print(f"Raíz 1: {raiz1}")
        print(f"Raíz 2: {raiz2}")
    elif discriminante == 0:
        raiz_unica = -coeficiente_b / (2 * coeficiente_a)
        print("\nEl polinomio tiene un raíz real (doble):")
        print(f"Raíz única: {raiz_unica}")
    else:
        print("\nEl polinomio no tiene raices reales. sus raíces son complejas.")

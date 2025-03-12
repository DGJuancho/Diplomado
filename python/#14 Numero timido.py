"""Un número se considera “tímido” si sus dígitos suman exactamente 10. Dado
un entero positivo n , devuelve el n-ésimo número “tímido”. Por ejemplo,
dado 1, deberías devolver 19. Dado 2, deberías devolver 28."""

numero = int(input("Por favor ingrese un número entero positivo del 1 al 9: "))

for n in range(1, 10):
    timido = numero + n
    if timido == 10:
        print(f"El número tímido de: {numero} es {str(numero) + str(n)}")

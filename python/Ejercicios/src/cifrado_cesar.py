def cifrar(texto, desplazamiento):
    """
    Cifra un texto usando el Cifrado César.
    Funciona para letras mayúsculas y minúsculas.
    """
    texto_cifrado = ""
    desplazamiento = (
        desplazamiento % 26
    )  # Asegura que el desplazamiento esté entre 0 y 25

    for caracter in texto:
        # Paso 1: Verificar si el caracter es una letra
        if "a" <= caracter.lower() <= "z":

            # Paso 2: Determinar la base (mayúscula o minúscula)
            if caracter.islower():
                base = ord("a")  # Base para minúsculas
            else:
                base = ord("A")  # Base para mayúsculas

            # Paso 3: Calcular la nueva posición de la letra
            posicion_original = ord(caracter) - base
            nueva_posicion = (posicion_original + desplazamiento) % 26

            # Paso 4: Convertir la nueva posición de vuelta a un caracter
            nuevo_caracter = chr(base + nueva_posicion)
            texto_cifrado += nuevo_caracter
        else:
            # Si no es una letra, simplemente lo añadimos al resultado
            texto_cifrado += caracter

    return texto_cifrado


# --- Lógica principal del programa ---
print("BIENVENIDO AL CIFRADO CÉSAR")

while True:
    try:
        opcion = int(input("\nEscoja una opción:\n1. Cifrar\n2. Descifrar\n3. Salir\n"))

        if opcion == 1:
            texto_usuario = input("\nIntroduce el texto a cifrar: ")
            desplazamiento_usuario = int(
                input("Introduce el número de desplazamiento: ")
            )
            resultado = cifrar(texto_usuario, desplazamiento_usuario)
            print(f"\nTexto cifrado: {resultado}")

        elif opcion == 2:
            texto_usuario = input("\nIntroduce el texto a descifrar: ")
            desplazamiento_usuario = int(
                input("Introduce el número de desplazamiento: ")
            )
            # Para descifrar, simplemente usamos un desplazamiento negativo
            resultado = cifrar(texto_usuario, -desplazamiento_usuario)
            print(f"\nTexto descifrado: {resultado}")

        elif opcion == 3:
            print("Saliendo del programa.")
            break

        else:
            print("Opción incorrecta. Por favor, elige 1, 2 o 3.")

    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

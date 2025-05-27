# Esta función separa el número binario del resto de la cadena
def separar_binarios(string):
    bin_dig = ""
    new_string = ""
    for caracter in string:
        if caracter == "0" or caracter == "1":
            bin_dig += caracter
        else:
            new_string += caracter
    return bin_dig, new_string


# Esta función convierte el número binario en decimal
def decimal(binario):
    num_decimal = 0
    for indice, digito in enumerate(binario[::-1]):
        num_decimal += int(digito) * 2**indice
    return num_decimal


string = input("Por favor ingrese un string: ")
binario, cadena = separar_binarios(string)
num_decimal = decimal(binario)

if num_decimal % 2 == 0:
    print(num_decimal)
else:
    print(cadena)

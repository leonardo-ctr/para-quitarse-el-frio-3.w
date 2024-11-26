
# Solicitar al usuario que ingrese un número binario
binario = input("Ingresa un número binario: ")

# Validar que el número binario solo contenga 0s y 1s
if all(c in '01' for c in binario):
    # Convertir el número binario (cadena) a entero
    entero = int(binario, 2)
    # Mostrar el resultado
    print(f"El número binario {binario} en decimal es: {entero}")
else:
    print("Error: El número ingresado no es binario válido.")
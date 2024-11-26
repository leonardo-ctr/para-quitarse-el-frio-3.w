
# Solicitar al usuario que ingrese una cadena
cadena = input("Ingresa una cadena: ")

# Inicializamos el contador de letras mayúsculas
contador_mayusculas = 0

# Recorremos cada carácter de la cadena
for caracter in cadena:
    # Comprobamos si el carácter es una letra mayúscula
    if caracter.isupper():
        contador_mayusculas += 1

# Mostrar el resultado
print(f"La cantidad de letras mayúsculas en la cadena es: {contador_mayusculas}")
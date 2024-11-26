
def contar_vocales(palabra):
    # Inicializar un diccionario para contar las vocales
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Recorrer cada letra de la palabra y contar las vocales
    for letra in palabra.lower():  # Convertir a minúsculas para que no distinga entre mayúsculas y minúsculas
        if letra in vocales:
            vocales[letra] += 1
    
    return vocales

# Solicitar al usuario que ingrese una palabra
palabra_usuario = input("Ingresa una palabra: ")

# Contar las vocales en la palabra ingresada
vocales_contadas = contar_vocales(palabra_usuario)

# Imprimir los resultados
print(f"Las vocales en la palabra '{palabra_usuario}' son:")
for vocal, cantidad in vocales_contadas.items():
    print(f"{vocal.upper()}: {cantidad}")
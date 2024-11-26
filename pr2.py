
def mas_larga(palabras):
    # Inicializamos la palabra más larga como la primera de la lista
    palabra_larga = palabras[0]
    
    # Recorremos todas las palabras de la lista
    for palabra in palabras:
        # Si encontramos una palabra más larga, la actualizamos
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra
    
    return palabra_larga
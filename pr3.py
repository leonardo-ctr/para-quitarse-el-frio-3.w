
print(" ")
def filtrar_palabras(palabras, n):
    return [palabra for palabra in palabras if len(palabra) > n]

palabras = ["manzana", "sol", "elefante", "gato", "perro"]
resultado = filtrar_palabras(palabras, 4)
print(resultado) 
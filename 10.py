def es_bisiesto(anio):
    # Un año es bisiesto si es divisible por 4, pero no por 100, excepto si es divisible por 400
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

# Ejemplo de uso
anio_usuario = int(input("Ingresa un año para verificar si es bisiesto: "))
if es_bisiesto(anio_usuario):
    print(f"El año {anio_usuario} es bisiesto.")
else:
    print(f"El año {anio_usuario} no es bisiesto.")
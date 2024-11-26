
def max_in_list(numeros):
    # Inicializamos el máximo con el primer número de la lista
    max_num = numeros[0]
    
    # Recorremos todos los números de la lista
    for num in numeros:
        # Si encontramos un número mayor que el actual máximo, lo actualizamos
        if num > max_num:
            max_num = num
            
    return max_num
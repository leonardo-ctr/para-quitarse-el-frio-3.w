
# Definir una tupla con 10 edades de personas
edades = (18, 25, 30, 22, 19, 45, 16, 33, 27, 21)

# Contar cuántas personas tienen edades superiores a 20
personas_mayores_20 = sum(1 for edad in edades if edad > 20)

# Imprimir el resultado
print(f"Cantidad de personas con edades superiores a 20: {personas_mayores_20}")
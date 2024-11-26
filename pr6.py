
# Solicitar el año en curso
anio_actual = int(input("Ingresa el año en curso: "))

# Lista para almacenar los nombres y años de nacimiento de las personas
personas = []

# Ingresar la información de tres personas
for i in range(3):
    nombre = input(f"Ingresa el nombre de la persona {i+1}: ")
    anio_nacimiento = int(input(f"Ingresa el año de nacimiento de {nombre}: "))
    personas.append((nombre, anio_nacimiento))

# Calcular y mostrar la edad que cumplirán en el año en curso
print("\nEdad que cumplirán las personas en el año en curso:")
for persona in personas:
    nombre, anio_nacimiento = persona
    edad = anio_actual - anio_nacimiento
    print(f"{nombre} cumplirá {edad} años en el año {anio_actual}.")
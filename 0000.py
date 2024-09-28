# a. Crear un diccionario que representa a una persona
def crear_estudiante(nombre, dni, edad):
    return {
        'nombre': nombre,
        'dni': dni,
        'edad': edad,
        'curso': {}  # Este campo será otro diccionario
    }

# b. Agregar un curso al diccionario del estudiante
def agregar_curso(estudiante, año, division, orientacion):
    estudiante['curso'] = {
        'año': año,
        'division': division,
        'orientacion': orientacion
    }

# c. Buscar la persona con mayor edad en la lista de estudiantes
def encontrar_mayor_edad(estudiantes):
    if not estudiantes:
        return None
    return max(estudiantes, key=lambda x: x['edad'])

# Lista de estudiantes
estudiantes = []

# Agregar estudiantes a la lista
estudiante1 = crear_estudiante("Ana Pérez", "12345678", 20)
agregar_curso(estudiante1, 2023, "A", "Ciencias Sociales")
estudiantes.append(estudiante1)

estudiante2 = crear_estudiante("Luis Gómez", "87654321", 22)
agregar_curso(estudiante2, 2023, "B", "Matemáticas")
estudiantes.append(estudiante2)

estudiante3 = crear_estudiante("María López", "13579246", 19)
agregar_curso(estudiante3, 2023, "A", "Ciencias Naturales")
estudiantes.append(estudiante3)

# Buscar e imprimir la persona con mayor edad
mayor_edad = encontrar_mayor_edad(estudiantes)
if mayor_edad:
    print("El estudiante con mayor edad es:")
    print(mayor_edad)
else:
    print("No hay estudiantes en la lista.")

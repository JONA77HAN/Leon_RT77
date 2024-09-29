# diccionarios de plantas ejercicio pensamiento

def guardar_planta(plantas, especie, necesita_luz, precio):
    planta_nueva = {
        'especie': especie,
        'necesita_luz': necesita_luz,
        'precio': precio
    }
    plantas.append(planta_nueva)

plantas = []
guardar_planta(plantas, 'Rosa', True, 4500)

print(plantas)
        
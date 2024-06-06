datos_curiosos = [
    "Los pulpos tienen tres corazones.",
    "Las avestruces pueden correr más rápido que los caballos.",
    "Los osos polares son zurdos.",
    "El ojo del avestruz es más grande que su cerebro.",
    "Los pingüinos pueden saltar hasta 6 pies en el aire.",
    "Las mariposas pueden saborear con sus pies.",
    "Las jirafas tienen la misma cantidad de huesos en el cuello que los humanos.",
    "Los cocodrilos no pueden sacar la lengua.",
    "Los elefantes son los únicos animales que no pueden saltar.",
    "Las cebras tienen rayas únicas, al igual que las huellas dactilares humanas.",
    "Los camaleones pueden mover sus ojos en dos direcciones al mismo tiempo.",
    "Las hormigas nunca duermen.",
    "Las abejas pueden detectar explosiones de TNT.",
    "Los tigres tienen rayas en la piel, no solo en el pelaje.",
    "Los koalas duermen alrededor de 22 horas al día.",
    "Los flamencos pueden doblar sus rodillas hacia atrás.",
    "Los caballos tienen la capacidad de vomitar.",
    "Los pingüinos solo tienen una pareja de apareamiento por año y se mantienen fieles a ella.",
    "Las arañas no son insectos, son arácnidos.",
    "Las luciérnagas no son realmente moscas, son escarabajos.",
    "Los cocodrilos son excelentes padres y pueden llevar a sus bebés en su boca.",
    "Los gatos tienen 32 músculos en cada oreja.",
    "Los lobos tienen un aullido distintivo que les permite reconocer a los miembros de su manada.",
    "Las serpientes no tienen párpados.",
    "Los delfines pueden usar burbujas de aire para jugar.",
    "Los ratones prefieren el queso a otros alimentos debido a su alto contenido de grasa.",
    "Los lobos tienen un sentido del olfato extremadamente agudo y pueden oler a su presa a kilómetros de distancia.",
    "Las nutrias marinas pueden dormir cogidas de la mano de otra nutria para evitar ser arrastradas por las corrientes.",
    "Las iguanas pueden mantener la respiración bajo el agua durante 28 minutos.",
    "Los camellos tienen párpados gruesos y largas pestañas para proteger sus ojos de las tormentas de arena.",
    "Las vacas tienen mejores amigos y pueden experimentar estrés si se separan de ellos.",
    "Los murciélagos son los únicos mamíferos capaces de volar.",
    "Los erizos flotan en el agua.",
    "Los cisnes se quedan con la misma pareja toda su vida.",
    "Los búhos pueden girar sus cabezas 270 grados.",
    "Los alces son excelentes nadadores y pueden cruzar cuerpos de agua largos y profundos.",
    "Los osos polares son zurdos.",
    "Los patos tienen penes en forma de espiral.",
    "Los chimpancés pueden aprender a reconocerse en un espejo.",
    "Los perros sudan a través de sus patas.",
    "Los pingüinos tienen glándulas especiales que les permiten beber agua de mar.",
    "Las vacas pueden dormir de pie, pero solo entrarán en un sueño REM cuando estén tumbadas.",
    "Los elefantes pueden comunicarse a largas distancias a través de sonidos de baja frecuencia.",
    "Las moscas domésticas pueden detectar un golpe con la rapidez de un parpadeo.",
    "Los armadillos pueden caminar bajo el agua.",
    "Las jirafas nacen con cuernos óseos en la cabeza.",
    "Los canguros pueden saltar hasta 3 veces su propia longitud.",
    "Las abejas pueden ver colores en el espectro ultravioleta.",
    "Los pingüinos pueden saltar hasta 6 pies en el aire."
]

def mostrar_datos_curiosos(datos):
    print("¡Bienvenido al juego de datos curiosos!")
    print("Aquí tienes algunos datos interesantes para ti:")

    for i, dato in enumerate(datos):
        print(f"{i+1}. {dato}")
        decision = input("¿Quieres ver otro dato curioso? (s/n): ").lower()
        if decision != "s":
            print("¡Espero que hayas disfrutado de los datos curiosos!")
            break

mostrar_datos_curiosos(datos_curiosos)

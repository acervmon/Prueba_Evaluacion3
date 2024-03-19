class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __str__(self):
        return f"{self.nombre} - {self.longitud} metros - {self.tripulantes} tripulantes - {self.pasajeros} pasajeros"

def agregar_nave(naves):
    nombre = input("Ingrese el nombre de la nave: ")
    longitud = int(input("Ingrese la longitud de la nave en metros: "))
    tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
    pasajeros = int(input("Ingrese la cantidad de pasajeros: "))
    nave = NaveEspacial(nombre, longitud, tripulantes, pasajeros)
    naves.append(nave)


def ordenar_naves(naves):
    naves.sort(key=lambda nave: (nave.nombre, -nave.longitud))


def mostrar_nave(naves, nombre):
    for nave in naves:
        if nave.nombre == nombre:
            print(nave)


def naves_mayor_pasajeros(naves):
    naves_ordenadas = sorted(naves, key=lambda nave: -nave.pasajeros)
    return naves_ordenadas[:5]


def nave_mayor_tripulantes(naves):
    tripulantes_max = max(naves, key=lambda nave: nave.tripulantes).tripulantes
    naves_mayor_tripulantes = [nave for nave in naves if nave.tripulantes == tripulantes_max]
    return naves_mayor_tripulantes


def mostrar_naves(naves):
    print("Tabla de naves:")
    print("Nombre - Longitud - Tripulantes - Pasajeros")
    for nave in naves:
        print(nave)

def eliminar_nave(naves):
    nombre = input("Ingrese el nombre de la nave que desea eliminar: ")
    for nave in naves:
        if nave.nombre == nombre:
            naves.remove(nave)
            print("Nave eliminada exitosamente.")
            return
    print("No se encontró la nave con el nombre ingresado.")

if __name__ == "__main__":
    lista_naves = []

# Agregar naves iniciales
    cometa_veloz = NaveEspacial("Cometa Veloz", 10000, 3210, 50)
    titan_del_cosmos = NaveEspacial("Titán del Cosmos", 221300, 120, 100)
    lista_naves.append(cometa_veloz)
    lista_naves.append(titan_del_cosmos)

    # Mostrar información de las naves iniciales
    print("Información de las naves iniciales:")
    mostrar_naves(lista_naves)
    print()

    print("1. Ordenar naves")
    print("2. Mostrar información de Cometa Veloz y Titán del Cosmos")
    print("3. Naves con mayor cantidad de pasajeros")
    print("4. Nave con mayor cantidad de tripulantes")
    print("5. Mostrar naves cuyo nombre comienza con 'GX'")
    print("6. Mostrar naves con seis o más pasajeros")
    print("7. Mostrar información de la nave más pequeña y la más grande")
    print("8. Agregar nueva nave")
    print("9. Eliminar nave agregada recientemente")
    print("10. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        ordenar_naves(lista_naves)
        mostrar_naves(lista_naves)
    elif opcion == "2":
        mostrar_nave(lista_naves, "Cometa Veloz")
        mostrar_nave(lista_naves, "Titán del Cosmos")
    elif opcion == "3":
        naves_pasajeros = naves_mayor_pasajeros(lista_naves)
        for nave in naves_pasajeros:
            print(nave)
    elif opcion == "4":
        naves_tripulantes = nave_mayor_tripulantes(lista_naves)
        for nave in naves_tripulantes:
            print(nave)
    elif opcion == "5":
        naves_gx = [nave for nave in lista_naves if nave.nombre.startswith("GX")]
        for nave in naves_gx:
            print(nave)
    elif opcion == "6":
        naves_pasajeros_seis_mas = [nave for nave in lista_naves if nave.pasajeros >= 6]
        for nave in naves_pasajeros_seis_mas:
            print(nave)
    elif opcion == "7":
        naves_ordenadas_longitud = sorted(lista_naves, key=lambda nave: nave.longitud)
        nave_mas_pequena = naves_ordenadas_longitud[0]
        nave_mas_grande = naves_ordenadas_longitud[-1]
        print("Nave más pequeña:")
        print(nave_mas_pequena)
        print("Nave más grande:")
        print(nave_mas_grande)
    elif opcion == "8":
        agregar_nave(lista_naves)
        mostrar_naves(lista_naves)
    elif opcion == "9":
        eliminar_nave(lista_naves)
        mostrar_naves(lista_naves)
    elif opcion == "10":
        print("Saliendo...")
    else:
        print("Opción inválida. Intente nuevamente.")

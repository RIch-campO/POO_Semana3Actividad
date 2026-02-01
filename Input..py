def menu():
    print("--- MENU ---\n")
    print("1. Saludar")
    print("2. Salir")
    opcion = input("Seleccione una opcion: ")
    return opcion

while True:
    opcion = menu()
    if opcion == "1":
        print("Hola! estás usando una CLI en Python")

    elif opcion == "2":
        break

    else:
        print("Opcion no valida")

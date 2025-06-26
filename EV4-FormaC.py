#-----INICIACION DE VARIABLES-----
compradores_fortificados = []
compradores_iluminados = []

stock_fortificados = 500
stock_iluminados = 500
#-----INICIACION DE VARIABLES-----

#---------------------------FUNCIONES---------------------------------------------
def validar_codigo_fortificados(codigo):
    if len(codigo) < 6:
        return False
    tiene_mayuscula = False
    tiene_numero = False
    for i in codigo:
        if i.isupper():
            tiene_mayuscula = True
        if i.isdigit():
            tiene_numero = True
        if i == " ":
            return False
    return tiene_mayuscula and tiene_numero

def validar_codigo_iluminados(codigo):
    if len(codigo) < 5:
        return False
    mayusculas = 0
    tiene_numero = False
    for i in codigo:
        if i.isupper():
            mayusculas += 1
        if i.isdigit():
            tiene_numero = True
        if i == " ":
            return False
    return mayusculas >= 3 and tiene_numero

def comprar_fortificados():
    global stock_fortificados
    if stock_fortificados == 0:
        print("No quedan entradas disponibles.")
        return

    nombre = input("Ingrese nombre de comprador: ")
    if nombre in compradores_fortificados:
        print("Este nombre ya compró entrada.")
        return

    tipo = input("Ingrese tipo de entrada (G o V): ").upper()
    if tipo != "G" and tipo != "V":
        print("Tipo de entrada inválido.")
        return

    while True:
        codigo = input("Ingrese código de confirmación: ")
        if validar_codigo_fortificados(codigo):
            print("Código validado.")
            break
        else:
            print("Código no válido. Intente otra vez.")

    compradores_fortificados.append(nombre)
    stock_fortificados -= 1
    print("¡Entrada registrada con éxito para 'Los Fortificados'!")

def comprar_iluminados():
    global stock_iluminados
    if stock_iluminados == 0:
        print("No quedan entradas disponibles.")
        return

    nombre = input("Ingrese nombre de comprador: ")
    if nombre in compradores_iluminados:
        print("Este nombre ya compró entrada.")
        return

    tipo = input("Ingrese tipo de entrada (CV o PAL): ").upper()
    if tipo != "CV" and tipo != "PAL":
        print("Tipo de entrada inválido.")
        return

    while True:
        codigo = input("Ingrese código de confirmación: ")
        if validar_codigo_iluminados(codigo):
            print("Código validado.")
            break
        else:
            print("Código no válido. Intente otra vez.")

    compradores_iluminados.append(nombre)
    stock_iluminados -= 1
    print("¡Entrada registrada con éxito para 'Los Iluminados'!")

def mostrar_stock():
    print("Entradas disponibles para 'Los Fortificados':", stock_fortificados)
    print("Entradas disponibles para 'Los Iluminados':", stock_iluminados)
#---------------------------FUNCIONES---------------------------------------------

#---------------------------MENU PRINCIPAL---------------------------------------------
def menu():
    while True:
        print("\nTOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE")
        print("1.- Comprar entrada a 'Los Fortificados'")
        print("2.- Comprar entrada a 'Los Iluminados'")
        print("3.- Ver stock de entradas")
        print("4.- Salir")
        
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            comprar_fortificados()
        elif opcion == "2":
            comprar_iluminados()
        elif opcion == "3":
            mostrar_stock()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

menu()
#---------------------------MENU PRINCIPAL---------------------------------------------
#---------------------------------------DICCIONARIO-------------------------------------
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050']
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}
#---------------------------------------DICCIONARIO-------------------------------------

#---------------------------------------FUNCIONES---------------------------------------
def stock_marca(marca):
    total = 0
    marca = marca.lower()
    for i in productos:
        if productos[i][0].lower() == marca:
            if i in stock:
                total += stock[i][1]
    print("El stock es:", total)

def buscar_precio(p_min, p_max):
    encontrados = []
    for i in stock:
        precio, cantidad = stock[i]
        if cantidad > 0 and p_min <= precio <= p_max:
            if i in productos:
                marca = productos[i][0]
                encontrados.append(f"{marca}--{i}")
    if len(encontrados) == 0:
        print("No hay notebooks en ese rango de precios.")
    else:
        print("Los notebooks entre los precios consultados son:", sorted(encontrados))

def listar_productos():
    if not productos:
        print("No hay notebook disponibles para mostrar")
        return

    print("------- Listado de Notebooks Ordenados --------")
    ordenados = sorted(productos.items(), key=lambda x: x[1][0])  # ordena por marca
    for i, z in ordenados:
        marca = z[0]
        ram = z[2]
        disco = z[4]
        print(f"{marca} - {i} - {ram} - {disco}")
    print("------------------------------------------------")
#---------------------------------------FUNCIONES-------------------------------------

#---------------------------------------MENU------------------------------------------
def menu():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Listado de productos.")
        print("4. Salir.")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)

        elif opcion == "2":
            while True:
                try:
                    precio_min = int(input("Ingrese precio mínimo: "))
                    precio_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            buscar_precio(precio_min, precio_max)

        elif opcion == "3":
            listar_productos()

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción válida!!")

menu()
#---------------------------------------MENU------------------------------------------
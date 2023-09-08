#Confesionar un programa que permita cargar un codigo de producto como
#clave en un diccionario. Guardar para dicha clave el nombre del productos,
#su precio y cantidad en stock.
#Implementar las siguientes actividades.
#1) Cargar de datos en el diccionario.
#2) Listado completo de productos
#3) Consulta de un producto por su clavo, mostrar el nombre, precio y stock
#4) Listado de todos los productos que tengan un stock con valor cero.

def cargar():
    productos={}
    continua="s"
    while continua=="s":
        codigo=int(input("Ingrese el codigo del producto:"))
        descripcion=input("Ingrese la descripcion:")
        precio=float(input("Ingrese el precio:"))
        stock=int(input("Ingrese el stock actual:"))
        productos[codigo]=(descripcion,precio,stock)
        continua=input("Desea carga otro producto[s/n]?")
    return productos

def imprimir(productos):
    print("Listado completo de productos:")
    for codigo in productos:
        print(productos[codigo][0],productos[codigo][1],productos[codigo][2])

def listado_stock_cero(productos):
    print("Listado de articulos con stock en cero:")
    for codigo in productos:
        if productos[codigo][2]==0:
            print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])

# bloque principal

productos=cargar()
imprimir (productos)
listado_stock_cero (productos)

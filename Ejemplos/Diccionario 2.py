#crear un diccionario que permita almacenar 5 articulos.
#utilizar como clave el nombre de producto y como valor el precio del mismo.
#Desarrollar ademas las funciones de:
#1) Imprimir en forma completa el diccionario
#2) Imprimir solo los articulos con precio superior a 100.

def cargar():
    productos={}
    for X in range(5):
        nombre=input("Ingrese el nombre del producto:")
        precio=int(input("Ingrese el precio:"))
        productos[nombre]=precio
    return productos

def imprimir(productos):
    print("Listado de todos los articulos")
    for nombre in productos:
        print(nombre, productos[nombre])

def imprimir_mayor100(productos):
    print("Listado de articulos con precios mayores a 100")
    for nombre in productos:
        if productos[nombre]>100:
            print(nombre)
        
# bloque principal

productos=cargar()
imprimir(productos)
imprimir_mayor100(productos)
        

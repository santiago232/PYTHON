#En el bloque principal del programa definir un diccionario que almacene
#los nombres de paises como clave y como valor la cantidad de habitaciones
#implentar una funcion para mostrar cada clave y valor.
def imprimir(paises):
    for clave in paises:
        print(clave,paises[clave])

# bloque principal

paises={"argentina":40000000, "españa'":4600000, "brasil":1900000, "uruguay":3400000}
imprimir(paises)

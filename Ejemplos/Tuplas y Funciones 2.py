#Desarrollsr una funcion que solicita la carga del dia, mes, año y
#almacene dichos datos en una tupla que luego debe retornar.
#La segunda funcion a implementar debe recibir una tupla
#con la fecha y mostrariam por pantalla.
def cargar_fecha():
    dd=int(input("Ingrese numero de dia:"))
    mm=int(input("Ingrese numero de mes:"))
    aa=int(input("Ingrese numeri de año"))
    return (dd,mm,aa)

def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")

# bloque principal

fecha=cargar_fecha()
imprimir_fecha(fecha)

    

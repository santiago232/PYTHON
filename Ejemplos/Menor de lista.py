#Crear y cargar una lista con 5 enteros por teclado.
#Implementar un algoritmo que identifique el menor valor de la lista y
#la posicion donde se encuentra.
lista=[]
for X in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

menor=lista[0]
posicion=0
for X in range(1, 5):
    if lista[X]<menor:
        menor=lista[X]
        posiciom=X
print("Lista completa")
print(lista)
print("Menor de la lista")
print(menor)
print("Posicion del menor en la lista")
print(posicion)

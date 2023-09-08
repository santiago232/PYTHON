#Realizar la carga de valores enteros por teclado,
#almacenarios en una lista. Finalizar la carga de enteros al ingresar al cero.
#Mostrar finalmente el tamaño de la lista.
lista=[]
valor=int(input("Ingresar valor (0 para finalizar):"))
while valor!=0:
    lista.append(valor)
    valor=int(input("Ingresar valor (0 para finalizar):"))

print("Tamaño de la lista:")
print(len(lista))

#Creacion de lista 1
listaA =[10, 2, 3, 4]
#Creacion de lista 2
listaB =["a", "b", "c", "d"]
#zip sirve para unir listas 
zip(listaA, listaB)
print(list(zip(listaA, listaB)))

#Sortd para ordenarlistas con datos numericos 
lista1 = sorted(listaA)
lista2 = sorted(listaB)
#Impresion de datos y tomanod el numero maximo
print(max(list(zip(listaA, listaB))))

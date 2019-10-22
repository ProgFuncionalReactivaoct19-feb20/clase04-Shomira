
"""
Manejo de colecciones y tuplas


# Encontrar la siguiente estructura
#

[(4.333333333333333, 13, 'Ángel'), (4.666666666666667, 14, 'Ana')]

Dadas las siguientes estructuras

"""
#Datos 
paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
nombres = ["Luis", "Ángel", "José", "Ana"]
#union de  dos listas usando zip 
var = list(zip(paraleloA, nombres))
#uso de la funcion anonima para sacar promedios suma de notas y se le envia el zip creado 
var2 = (map(lambda x :(sum(x[0]), x[1], sum(x[0])/3), var))
#Filter qeu filtra los promedios menor a 5
funcion = filter( lambda x: x[2] <= 5, var2)
#Impresion de datos usando enviandole la funcion y imprimiendo en lista 
print(list(funcion))


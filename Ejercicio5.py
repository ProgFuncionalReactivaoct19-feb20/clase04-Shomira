"""
Manejo de colecciones y tuplas


# Encontrar la siguiente estructura
#

[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]
(16.666666666666668, 'José')
[(13.0, 'Ana'), (16.666666666666668, 'José'), (16.333333333333332, 'Ángel')]

Dadas las siguientes estructuras

"""

paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]
prom = lambda x : sum(x)/3
#union y impresion de dos listas usando zip 
#map para aplicar a una funcion un argumento 
print(list(zip(map(prom,paraleloA), nombres)))
#Almacena 
var = list(zip(map(prom,paraleloA), nombres))
#Key nos permite que no solo se ordene  desde la posicion uno
print(sorted(var, key=lambda x: x[1]))
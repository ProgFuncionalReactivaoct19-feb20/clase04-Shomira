
"""
Manejo de colecciones y tuplas


# Encontrar la siguiente estructura
#

[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]

Dadas las siguientes estructuras:

"""
#lista de datos 
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]

nombres = ["Ángel", "José", "Ana"]
#Funcion anonima usada, uso del sum que suma los valores de las posiciones 
prom = lambda x : sum(x)/3

#Impresion de datos usando Zip y map 
print(list(zip(nombres, map(prom,paraleloA))))


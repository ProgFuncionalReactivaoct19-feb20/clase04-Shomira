'''
Manejo de coleciones y tuplas
'''
#Encontrar la siguiente estructura
#[('a', (30, 1)), ('b', (100, 2)), ('c', (20, 4))]

lista = [(100, 2), (20, 4), (30, 1)]
lista2 =  ["b", "a", "c"]

#Muestra la tupla tomando en cuenta la posicion 1 de la lista y le hace un sorted
print(list(zip(sorted(lista2),sorted(lista, key = lambda x:x[1]))))


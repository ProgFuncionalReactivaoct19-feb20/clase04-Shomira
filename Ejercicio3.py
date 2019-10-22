

#Encontrara l siguiente estructura 
#[((20, 4), "c"), ((30, 1), "B"), ((100, 2), "A")]
lista = [(100, 2), (20, 4), (30, 1)]
lista2 = ["b", "a", "c"]
#Funcion anonima que accaede a la posicion 0 de las listas 
listaA = lambda x:x[0]
#Upper para convertir en mayusculas al lista 
mayus = lambda x :x.upper()
#Impresion de datos usadno un sorted para ordenar y se le envia parametros y funciones 
print(list(zip(sorted(lista, key=listaA), sorted(map(mayus, lista2), reverse=True))))
#reverse = True ....para cadenas
#sorted para numeros
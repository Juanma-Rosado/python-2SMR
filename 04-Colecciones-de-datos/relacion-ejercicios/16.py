# Ejercicio 16
# Imprimir los árboles de la lista hasta que aparezca ficus.
# En caso de que no se encuentre ficus en la lista, al finalizar,
# imprimir por pantalla: El árbol ficus no está en la lista.

arboles = ["manzano","pino","madroño","eucalipto","nogal","olivo","almendro"]


for i in arboles:
    if i == "ficus":
        break
    print(i)
else:
    print("El árbol ficus no está en la lista")

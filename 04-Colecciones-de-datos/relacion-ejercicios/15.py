# Ejercicio 15
# Imprimir los árboles de la lista hasta que aparezca nogal.
# Utiliza la variable arboles = ["manzano", "pino", "madroño", "eucalipto",
# "nogal", "olivo", "almendro"].

arboles = ["manzano","pino","madroño","eucalipto","nogal","olivo","almendro"]

for arbol in arboles:
    if arbol=="nogal":
        break
    else:
        print(arbol)
# Dibuja un rectángulo de asteriscos con un ancho y alto que introduzca el usuario.

ancho=int(input("Introduce el ancho del rectangulo: "))
alto=int(input("Introduce el alto del rectangulo: "))

for fila in range(alto):
    print(ancho*"*")




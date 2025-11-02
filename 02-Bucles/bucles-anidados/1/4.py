# Cuadro con borde de asteriscos:
# Imprime un rectángulo de n x m formado por asteriscos, dejando el interior vacío (solo el borde con *).

h=int(input("Introduce alto: "))
l=int(input("Introduce largo: "))

for filas in range(h):
    if filas==0 or filas==h-1:
        print(l*"*")
    else:
        print("")
    for columnas in range(l):
        pass
    
    
    
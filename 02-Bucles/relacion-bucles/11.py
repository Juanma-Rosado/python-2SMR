# Pide al usuario que escriba su nombre cinco veces y
# muestra todos los nombres en una sola línea separados por comas.



""" nombres=[]

for _ in range(5):
    nombre=input("Introduzca su nombre: ")
    nombres.append(nombre)

print(", ".join(nombres)) """



nombres = ""

for i in range(5):
    nombre = input("Introduzca su nombre: ")
    if i == 0:
        nombres = nombre
    else:
        nombres = f"{nombres}, {nombre}"

print(f"Los nombres introducidos son: {nombres}")

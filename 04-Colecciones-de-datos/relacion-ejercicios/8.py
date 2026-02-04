# Ejercicio 8
# Imprimir la tabla de multiplicar de un número almacenado en una variable
# utilizando rangos. La salida para el número 5 sería:
# 5 * 1 = 5
# 5 * 2 = 10
# ...

numero=5

for i in range(1,11):
    print(f"{numero} * {i} = {numero*i}")
    

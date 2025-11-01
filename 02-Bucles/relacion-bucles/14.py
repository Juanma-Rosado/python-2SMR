# Pide un número y muestra la tabla de multiplicar del 1 hasta ese número.

numero = int(input("Introduce un número: "))

for n in range(1, numero + 1):
    print(f"\nTabla del {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")



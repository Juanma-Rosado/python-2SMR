altura = 5
for fila in range(1, altura + 1):
    # primero los espacios
    for e in range(altura - fila):
        print(" ", end="")
    # luego los asteriscos
    for a in range((fila * 2) - 1):
        print("*", end="")
    print()

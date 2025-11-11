contador=1

for fila in range(5):
    for columna in range(5):
        print(f"{contador:2}", end=" ")
        contador+=1
    print()
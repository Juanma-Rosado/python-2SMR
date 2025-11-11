import os
os.system("cls")

try:
    numero=int(input("Introduce un numero: "))

    for i in range(1, numero+1):
        for j in range(1, i+1):
            print(j, end="")
        print()
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
finally:
    print("El programa ha finalizado.")    

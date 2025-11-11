import random
import os
os.system("cls")

try:
    aleatorio=random.randint(1,10)
    numero=int(input("Adivina el numero (entre 1 y 10): "))

    while aleatorio!=numero:
        if numero>aleatorio:
            print("Demasiado alto")
        if numero<aleatorio:
            print("Demasiado bajo")
        numero=int(input("Adivina el numero (entre 1 y 10): "))
    else:
        print("¡Correcto!")
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
finally:
    print("El programa ha terminado.")
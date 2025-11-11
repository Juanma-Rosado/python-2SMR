import os
os.system("cls")

try:
    numero=int(input("Introduce un número (0 para terminar): "))
    contador=0
    suma=0

    while numero!=0:
        suma+=numero
        contador+=1
        numero=int(input("Introduce un número (0 para terminar): "))
    
    print(f"La media es {suma/contador}")
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
finally:
    print("El programa ha finalizado.")
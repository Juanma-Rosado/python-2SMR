import os
os.system("cls")

try:
    numero=int(input("Introduce un numero: "))
    contador=0

    if numero==0:
        contador=1
    else:
        while numero>0:
            numero=numero//10
            contador+=1
        
    print(f"El numero tiene {contador} digitos")

except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
finally:
    print("El programa ha finalizado")
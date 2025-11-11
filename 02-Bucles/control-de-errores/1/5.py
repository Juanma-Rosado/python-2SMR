import os
os.system("cls")

try:
    frase=input("Introduce una palabra o frase: ")
    contador=0

    for letra in frase:
        if letra=="a":
            contador+=1
    print(f"La letra 'a' aparece {contador} veces")
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
finally:
    print("El programa ha finalizado")

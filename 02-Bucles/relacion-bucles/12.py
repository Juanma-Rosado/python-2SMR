# Pide una frase y muestra cuántas veces aparece la letra “a”.

frase=input("Escribe una frase: ")
contador=0

for letra in frase:
    if letra=="a":
        contador+=1

print(f"Tu frase tiene {contador} letras a")
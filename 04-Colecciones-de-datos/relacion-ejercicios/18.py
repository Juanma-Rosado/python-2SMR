# Ejercicio 18
# Definir una función que, al recibir una cadena de texto, cuente
# cuántas vocales hay y devuelva dicho valor.
# Dada la cadena, imprimir La cantidad de vocales en el texto es:.

def vocales(texto):
    voc="aeiou"
    num_vocales=0
    for caracter in texto:
        if caracter in voc:
            num_vocales+=1
    return num_vocales

x = "Estoy haciendo un curso de Python"
print(f"La cantidad de vocales en el texto es: {vocales(x)}")
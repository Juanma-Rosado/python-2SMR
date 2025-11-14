def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Pedir al usuario los números
inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))

print(f"Números primos entre {inicio} y {fin}:")
for num in range(inicio, fin + 1):
    if es_primo(num):
        print(num, end=" ")

import random


numeros=[]
cuadrados=[]
cubos=[]

for _ in range(20):
    numeros.append(random.randint(0,100))

for n in numeros:
    cuadrados.append(n**2)
    cubos.append(n**3)


print(numeros)
print(cuadrados)
print(cubos)


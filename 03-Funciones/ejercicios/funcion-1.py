def suma(num1, num2):
    resultado=num1+num2
    return resultado

def resta(num1, num2):
    resultado=num1-num2
    return resultado

def multiplicacion(num1, num2):
    resultado=num1*num2
    return resultado

def division(num1, num2):
    resultado=num1/num2
    return resultado

def division_entera(num1, num2):
    resultado=num1//num2
    return resultado

def resto(num1, num2):
    resultado=num1%num2
    return resultado

def menu():
    print("----Opciones----")
    print("0. Salir")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Division entera")
    print("6. Resto")
    
menu()
opcion=None
while opcion!=0:
    opcion=input("Introduce una opcion: ")
    num1=int(input("Introduce un numero: "))
    num2=int(input("Introduce otro numero: "))
    if opcion==1:
        print(suma())
    elif opcion==2:
        print(resta())
    elif opcion==3:
        print(multiplicacion())
    elif opcion==4:
        print(division())
    elif opcion==5:
        print(division_entera())
    elif opcion==6:
        print(resta())
    
else:
    print("Programa finalizado.")
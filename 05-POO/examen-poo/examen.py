import os, carga_examen,clase_alumno

def menu():
    print ("_________________________________________________")
    print ("1.- Matricular un alumno.")
    print ("2.- Dar de baja un alumno.")
    print ("3.- Modificar datos de un alumno.")
    print ("4.- Consultar los datos de un alumno.")
    print ("5.- Listado de los alumnos del curso.")
    print ("6.- Añadir, modificar o borrar una nota a un alumno del curso.")
    print ("0.- Salir del programa.")
    opcion=input ("Elige una opción: ")
    return opcion

def submenu():
    print ("_________________________________________________")
    print ("1.- Añadir una nota a un alumno del curso.")
    print ("2.- Modificar una nota a un alumno del curso.")
    print ("3.- Borrar una nota a un alumno del curso.")
    print ("0.- Salir del programa.")
    opcion2=input ("Elige una opción: ")
    return opcion2

#---------------DESDE AQUÍ TE TOCA EMPEZAR A TRABAJAR

def matricula(lista):
    #Esta función se usa para añadir un alumno a la lista de alumnos.
    nombre=input("Dime el nombre del alumno a matricular: ")
    apellidos=input("Dime los apellidos del alumno a matricular: ")
    email=input("Dime el email del alumno a matricular: ")
    curso=input("Dime el curso del alumno a matricular: ")

    alumno=clase_alumno.Alumno(nombre,apellidos,email,curso)
    lista.append(alumno)
    
    return lista


def baja(lista, nombre):
    #Esta función se usa para borrar un alumno determinado de la lista de alumnos.
    for objeto in lista:
        if objeto.get_nombre()==nombre:
            lista.remove(objeto)
            print("Alumno desmatriculado")
            break
    else:
        print("Ese alumno no esta matriculado")

    return lista

def modifica(lista, nombre):
    #Esta función se usa para modificar los datos un alumno determinado de la lista de alumnos.
    #MIRA COMO FUNCIONA EN EL ENUNCIADO DEL PROGRAMA
    print("Los campos disponibles son: nombre, apellidos, email y curso")
    opcion=input("¿Cual quieres modificar?: ")
    
    for objeto in lista:
        if nombre==objeto.get_nombre():
            if opcion=="nombre":
                nuevo_nombre=input("Dime el nuevo nombre: ")
                objeto.set_nombre(nuevo_nombre)

            elif opcion=="apellidos":
                nuevos_apellidos=input("Dime los nuevos apellidos: ")
                objeto.set_apellidos(nuevos_apellidos)

            elif opcion=="email":
                nuevo_email=input("Dime el nuevo email: ")
                objeto.set_email(nuevo_email)

            elif opcion=="curso":
                nuevo_curso=input("Dime el nuevo curso: ")
                objeto.set_curso(nuevo_curso)
                
            else:
                print("Opcion invalida")
            
            break
    else:
        print("Ese alumno no esta matriculado")
        
    return lista


def consulta(lista, nombre):
    #Esta función se usa para mostrar los datos un alumno determinado de la lista de alumnos.
    #mira en el enunciado cómo se han de mostrar
    for objeto in lista:
        if nombre==objeto.get_nombre():
            objeto.consultar_datos_alumno()
            break
    else:
        print("Ese alumno no esta matriculado")


def listado(lista):
    #Esta función se usa para mostrar los datos de la lista de alumnos.
    #mira en el enunciado cómo se han de mostrar 
    print("----------Imprimiendo la lista de alumnos:------------------")
    contador=0
    for objeto in lista:
        objeto.listado_alumnos()
        contador+=1
    print(f"---------Número de alumnos procesados: {contador}------------")


def añadir_nota(lista, nombre):
    modulo=input("Introduce el módulo: ")
    nota=int(input("Introduce la nota: "))
    
    if modulo=="Fin":
        return lista
    
    for objeto in lista:
        if nombre==objeto.get_nombre():
            objeto.notas[modulo]=nota
            print("Nota añadida correctamente")
            break
    else:
        print("Ese alumno no esta matriculado")
    
    return lista


def modificar_nota(lista,nombre):
    modulo=input("Introduce el módulo: ")
    nota=int(input("Introduce la nota: "))
    
    if modulo=="Fin":
        return lista
    
    for objeto in lista:
        if nombre==objeto.get_nombre():
            objeto.notas[modulo]=nota
            print("Nota modificada correctamente")
            break
    else:
        print("Ese alumno no esta matriculado")
    
    return lista


def borrar_nota(lista,nombre):
    modulo=input("Introduce el módulo: ")
    
    if modulo=="Fin":
        return lista
    
    for objeto in lista:
        if nombre==objeto.get_nombre():
            del objeto.notas[modulo]
            print("Nota borrada correctamente")
            break
    else:
        print("Ese alumno no esta matriculado")
    
    return lista


#-------HASTA AQUÍ ES DONDE ESTÁ EL TRABAJO QUE TIENES QUE HACER EN ESTE ARCHIVO


#-------------------DESDE AQUÍ YA NO PUEDES TOCARLO
lista_curso=carga_examen.carga_lista()
opcion=0
while opcion !="0":
    os.system("cls")
    opcion=menu()
    match opcion:
        case "1": # matricular un alumno
            lista_curso=matricula(lista_curso)

        case "2": # dar de baja un alumno
            alumno=input("Dime el nombre del alumno a desmatricular: ")
            lista_curso=baja(lista_curso,alumno)

        case "3": # modificar datos de un alumno
            alumno=input("Dime el nombre del alumno a modificar: ")
            lista_curso=modifica(lista_curso,alumno)
      
        case "4": # consultar datos de un alumno, con el formato:
                #Alumno:
                #    Nombre: Paco 
                #    Apellidos: Pil Pérez
                #    email: ppp@g.educaand.es
                #    Curso: 2B
                #    Notas:
                #       SOR: 6
                #       SERRE: 2
                #       SEGIN: 9
                #       Programación: 2
                alumno=input("Dime el nombre del alumno a consultar: ")
                consulta(lista_curso,alumno)

        case "5":  #imprime por pantalla la lista de alumnos, con el formato
                    # ----------Imprimiendo la lista de alumnos:------------------
                    # Nombre: Paco, Apellidos: Pil Pérez, Cuenta: ppp@g.educaand.es, Curso: 2B
                    # Nombre: Carmen, Apellidos: Gil Pérez, Cuenta: cgp@g.educaand.es, Curso: 8h
                    # Nombre: Luis, Apellidos: Gómez Gómez, Cuenta: lggg.educaand.es, Curso: 2B
                    # ---------Número de alumnos procesados: 3------------
                listado(lista_curso)

        case "6":
            opcion2=submenu()
            if opcion2=="1":
                alumno=input("Dime el nombre del alumno: ")
                lista_curso=añadir_nota(lista_curso,alumno)
                
            elif opcion2=="2":
                alumno=input("Dime el nombre del alumno: ")
                lista_curso=modificar_nota(lista_curso,alumno)
                
            elif opcion2=="3":
                alumno=input("Dime el nombre del alumno: ")
                lista_curso=borrar_nota(lista_curso,alumno)
                
            else:
                print("Elige una opción valida")
        
          
        case "0":
            print()
            print("Ha elegido salir del progarma.")   
        case _ : 
            print("Esta opción no existe")
    print()
    input("Pulsa enter para continuar...")
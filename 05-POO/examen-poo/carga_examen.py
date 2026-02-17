import os
from clase_alumno import *
import pathlib
import re #para manejo de expresiones regulares

#de cada cada cadena que  la linea del fichero carga un alumno y lo añade a una lista
def leeLinea(listaAlumnos,linea, separadores, curso):
    # Crear un patrón de expresión regular con los separadores
    patron = "[" + re.escape("".join(separadores)) + "]"
    # Dividir la línea usando re.split
    campos = re.split(patron, linea)
    # eliminar espacios en blanco al inicio/final de cada parte
    campos = [campo.strip() for campo in campos]
  
   #['Pil Pérez', 'Paco', 'ppp@g.educaand.es', '2Asmr']
    alumno=Alumno(campos[1],campos[0], campos[2], curso)
    #alumno.printAlumno()
    listaAlumnos.append(alumno)

def carga_lista():
        os.system('cls')
        # archivo = input("¿Qué fichero quieres abrir? (Q para salir): " )
        archivo="2A.txt"
        try:
            fichero=abreFichero(archivo)
            listaAlumnos=[]
            # curso=input("¿De qué curso es el alumnado contenido en el fichero?: ")
            curso="2A SMR"
            leeSeneca(listaAlumnos,fichero,curso)
            fichero.close()
            print (f"El curso {curso} ha sico cargado con éxito.")
            input("Pulsa enter para continuar.")
            return listaAlumnos
        except Exception as excepcion:
            print (f"Algo no ha ido bien en la carga del archivo {fichero}: ", excepcion)
            print("Revisa el nombre del archivo con su extensión, y que esté en la misma carpeta que este fichero.")
            input("Pulsa enter para continuar.")
            
#cargar un fichero con el formato de descarga de séneca
def leeSeneca(listaAlumnos,fichero,curso):
    print ("Leyendo el archivo con formato Séneca.")
    
    try:
        #QUITAMOS LAS LÍNEAS DE CABECERA QUE NOS DA SÉNECA, QUE SON 8
        for i in range (0,8):
            fichero.readline()
        for linea in fichero.readlines():
            leeLinea(listaAlumnos,linea,[",","|"], curso)
    except Exception as excepcion:
            print ("Algo no ha ido bien en leeSeneca: ", excepcion)    
    #finally:
        # Esta sección es siempre ejecutada
        #print("Fin leeSeneca.")
#cargar un fichero con formato distinto al de séneca
def leePlano(fichero,curso):
    separador=input("¿Cuáles son los caracteres separadores de los campos?: ")
    print ("Leyendo el archivo con formato personalizado.")
    separadores=list(separador) #esto separa la cadena en una lista de caracteres
    print("separadores: ", end="")
    print(separadores)
    try:
        for linea in fichero.readlines():
            leeLinea(linea,separadores, curso)
    except Exception as excepcion:
            print ("Algo no ha ido bien en leePlano: ", type(excepcion))    
   # finally:
        # Esta sección es siempre ejecutada
    #    print("Fin leePlano.")

              
def abreFichero(archivo):
    valido = False
    while valido != True: 
        try:
            path=str(pathlib.Path(__file__).parent.resolve())
            fichero = open(path+"\\" + archivo,"r")#, encoding="utf-8")
            valido=True
            return fichero
        except Exception as excepcion:
             print ("Algo no ha ido bien en abreFichero: ", type(excepcion)) 
             print("Este archivo no es legible. Por favor, introduce uno distinto.")
             print("Si quieres detener el programa introduce Q o q.")
             archivo = input("¿Qué fichero quieres abrir?: " )
             if archivo == "Q" or archivo == "q":
                print ("Gracias por usar nuestro programa.")
                exit(0)
        #finally:
           # print("Fin abreFichero")
              
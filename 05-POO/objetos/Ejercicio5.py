class Alumno:
    def __init__(self,nombre,notas):
        self.nombre=nombre
        self.notas=notas


    def promedio(self):
        suma=0
        contador=0
        for nota in self.notas.values():
            suma+=nota
            contador+=1
        promedio=suma/contador
        return promedio


notas_alumno1={
    "Mates":10,
    "Lengua":10
}    


alumno1=Alumno("Juanma", notas_alumno1)


media=alumno1.promedio()


print(f"El promedio de {alumno1.nombre} es {media}")

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
        return suma/contador

notas={
    "mates": 8,
    "lengua": 5
}

alumno1=Alumno("Juanma",notas)

print(alumno1.promedio())
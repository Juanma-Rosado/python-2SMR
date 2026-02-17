# Definición de la clase Alumno
class Alumno:
    def __init__(self,nombre,apellidos,email,curso,notas={}):
        self.nombre=nombre
        self.apellidos=apellidos
        self.email=email
        self.curso=curso
        self.notas=notas
    
    def get_nombre(self):
        return self.nombre
    def set_nombre(self,nombre):
        self.nombre=nombre
    
    def get_apellidos(self):
        return self.apellidos
    def set_apellidos(self,apellidos):
        self.apellidos=apellidos
    
    def get_email(self):
        return self.email
    def set_email(self,email):
        self.email=email
    
    def get_curso(self):
        return self.curso
    def set_curso(self,curso):
        self.curso=curso
        
    def get_notas(self):
        return self.notas
    def set_notas(self,notas):
        self.notas=notas


    def consultar_datos_alumno(self):
        print(f"""
            Alumno:
                Nombre: {self.nombre} 
                Apellidos: {self.apellidos}
                email: {self.email}
                Curso: {self.curso}
                Notas: {"No hay notas" if self.notas=={} else self.notas}
        """)
    
    
    def listado_alumnos(self):
        print(f"Nombre: {self.nombre}, Apellidos: {self.apellidos}, Cuenta: {self.email}, Curso: {self.curso}")

    
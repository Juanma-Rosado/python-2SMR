class Tarea:
    def __init__(self,descripcion,completa=False):
        self.descripcion=descripcion
        self.completa=completa
    
    def marcar_finalizada(self):
        self.completa=True
    
    def set_descripcion(self,descripcion):
        self.descripcion=descripcion
        
    def get_descripcion(self):
        return self.descripcion
    

tarea1=Tarea("Tarea1")
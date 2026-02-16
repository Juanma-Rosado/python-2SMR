class Biblioteca:
    def __init__(self):
        self.libros=[]
        
    def agregar_libro(self,titulo):
        self.libros.append(titulo)
        
    def mostrar_libros(self):
        print(f"Catalogo de libros: {self.libros}")


biblioteca=Biblioteca()

biblioteca.agregar_libro("Don Quijote")
biblioteca.agregar_libro("El Principito")

biblioteca.mostrar_libros()
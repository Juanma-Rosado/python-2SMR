class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self,nombre):
        self.nombre=nombre
        
    def get_precio(self):
        return self.precio
    
    def set_precio(self,precio):
        self.precio=precio
    
carrito=[]

producto1=Producto("Pan",2)
producto2=Producto("Leche",4)
producto3=Producto("Huevos",6)

carrito.append(producto1)
carrito.append(producto2)
carrito.append(producto3)

suma=0
for producto in carrito:
    suma+=producto.precio

print(suma)
class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

carrito=[]

producto1=Producto("Pan",2)
producto2=Producto("Leche",4)
producto3=Producto("Huevos",6)

carrito.append(producto1)
carrito.append(producto2)
carrito.append(producto3)

total=0
for producto in carrito:
    total+=producto.precio
    
print(total)
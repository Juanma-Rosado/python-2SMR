class CarritoDeCompras:
    def __init__(self, productos=None):
        if productos is None:
            self.productos = []
        else:
            self.productos = productos

    def agregar_producto(self, nombre_producto):
        self.productos.append(nombre_producto)

    def ver_carrito(self):
        if self.productos == []:
            print("El carrito está desierto")
        else:
            print("Productos en el carrito:")
            for producto in self.productos:
                print(f"-{producto}")


carrito1 = CarritoDeCompras()
carrito1.agregar_producto("Monitor Gaming")
carrito1.agregar_producto("Teclado Mecánico")
carrito1.ver_carrito()

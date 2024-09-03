class Ingrediente:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Menu:
    def __init__(self, nombre, precio, ingredientes):
        self.nombre = nombre
        self.precio = precio
        self.ingredientes = ingredientes

class Pedido:
    def __init__(self):
        self.menus = []
        self.total = 0

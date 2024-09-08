from models import Ingrediente, Menu, Pedido

class Controlador:
    def __init__(self):
        self.stock_ingredientes = []
        self.menus_disponibles = []
        self.pedido_actual = Pedido()

    def agregar_ingrediente(self, nombre, cantidad):
        for ingrediente in self.stock_ingredientes:
            if ingrediente.nombre == nombre:
                ingrediente.cantidad += cantidad
                return
        nuevo_ingrediente = Ingrediente(nombre, cantidad)
        self.stock_ingredientes.append(nuevo_ingrediente)


    def eliminar_ingrediente(self, nombre):
        # Lógica para eliminar ingredientes
        pass

    def generar_boleta(self):
        # Lógica para generar la boleta
        pass

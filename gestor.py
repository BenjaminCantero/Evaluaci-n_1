from models import Ingrediente, Menu, Pedido

class Controlador:
    def __init__(self):
        self.stock_ingredientes = []
        self.menus_disponibles = []
        self.pedido_actual = Pedido()

    def agregar_ingrediente(self, nombre, cantidad):
        # Lógica para agregar o actualizar ingredientes
        pass

    def eliminar_ingrediente(self, nombre):
        # Lógica para eliminar ingredientes
        pass

    def generar_boleta(self):
        # Lógica para generar la boleta
        pass

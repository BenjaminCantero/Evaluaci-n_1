from models import Ingrediente, Menu, Pedido
from utils import generar_boleta

class Controlador:
    def __init__(self):
        self.stock_ingredientes = []
        self.menus_disponibles = []
        self.pedido_actual = Pedido()

    def agregar_ingrediente(self, nombre, cantidad):
        cantidad = int(cantidad)  # Asegúrate de convertir a entero después de validar
        for ingrediente in self.stock_ingredientes:
            if ingrediente.nombre == nombre:
                ingrediente.cantidad += cantidad
                return
        
        nuevo_ingrediente = Ingrediente(nombre, cantidad)
        self.stock_ingredientes.append(nuevo_ingrediente)


    def eliminar_ingrediente(self, nombre):
        self.stock_ingredientes = [ing for ing in self.stock_ingredientes if ing.nombre != nombre]


    def generar_boleta(self):
        generar_boleta(self.pedido_actual)


from gestor import Gestor
import validaciones
import utils

class Controlador:
    def __init__(self):
        # Inicializar el gestor de ingredientes/pedidos
        self.gestor = Gestor()

    def agregar_ingrediente(self, nombre, cantidad):
        # Validaciones antes de agregar el ingrediente
        if validaciones.validar_nombre(nombre) and validaciones.validar_cantidad(cantidad):
            self.gestor.agregar_ingrediente(nombre, cantidad)
        else:
            print("Error: Validación fallida")

    def eliminar_ingrediente(self, nombre):
        self.gestor.eliminar_ingrediente(nombre)

    def generar_boleta(self, pedido_actual):
        utils.generar_boleta(pedido_actual)

from gestor import Gestor
import validaciones
import utils

class Controlador:
    def __init__(self):
        # Inicializar el gestor de ingredientes/pedidos
        self.gestor = Gestor()
        self.ingredientes = []  # Lista para almacenar ingredientes si es necesario

    def agregar_ingrediente(self, nombre, cantidad):
        # Validaciones antes de agregar el ingrediente
        if validaciones.validar_nombre(nombre) and validaciones.validar_cantidad(cantidad):
            if not any(ingrediente['nombre'] == nombre for ingrediente in self.gestor.ingredientes):
                self.gestor.agregar_ingrediente(nombre, cantidad)
            else:
                print("Error: El ingrediente ya existe")
        else:
            print("Error: Validación fallida")

    def eliminar_ingrediente(self, nombre):
        # Elimina un ingrediente a través del gestor
        self.gestor.eliminar_ingrediente(nombre)

    def obtener_ingredientes(self):
        return self.gestor.obtener_ingredientes()

    def generar_boleta(self, pedido_actual):
        # Genera una boleta para el pedido actual utilizando utils
        utils.generar_boleta(pedido_actual)

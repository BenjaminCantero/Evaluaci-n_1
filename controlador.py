from gestor import Gestor
import validaciones
import utils

class Controlador:
    def __init__(self):
        self.gestor = Gestor()

    def agregar_ingrediente(self, nombre, cantidad):
        if validaciones.validar_nombre(nombre) and validaciones.validar_cantidad(cantidad):
            self.gestor.agregar_ingrediente(nombre, cantidad)
        else:
            print("Error: Validación fallida")

    def agregar_menu_al_pedido(self, menu):
        if self.gestor.verificar_stock(menu):
            self.gestor.descontar_ingredientes(menu)
            precio = self.gestor.menus[menu]['precio']
            self.gestor.agregar_pedido(menu, 1, precio)
        else:
            print(f"Error: No hay suficiente stock para preparar {menu}")

    def eliminar_menu_del_pedido(self, menu):
        self.gestor.reponer_ingredientes(menu)
        self.gestor.eliminar_menu(menu)

    def eliminar_ingrediente(self, nombre):
        self.gestor.eliminar_ingrediente(nombre)

    def generar_menus_disponibles(self):
        return self.gestor.generar_menus_disponibles()

    def generar_boleta(self, pedido_actual):
        utils.importar_boleta_desde_pdf(pedido_actual)  # Función que importará el PDF

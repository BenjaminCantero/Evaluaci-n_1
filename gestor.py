class Gestor:
    def __init__(self):
        self.ingredientes = []
        self.pedido_actual = []
        self.menus = {
            "Papas fritas": {"precio": 500, "ingredientes": {"papas": 5}},
            "Pepsi": {"precio": 1100, "ingredientes": {"bebida": 1}},
            "Completo": {"precio": 1800, "ingredientes": {"vienesa": 1, "pan de completo": 1, "tomate": 1, "palta": 1}},
            "Hamburguesa": {"precio": 3500, "ingredientes": {"pan de hamburguesa": 1, "queso": 1, "churrasco de carne": 1}}
        }

    def agregar_ingrediente(self, nombre, cantidad):
        for ingrediente in self.ingredientes:
            if ingrediente['nombre'] == nombre:
                ingrediente['cantidad'] += cantidad
                return
        self.ingredientes.append({'nombre': nombre, 'cantidad': cantidad})

    def eliminar_ingrediente(self, nombre):
        self.ingredientes = [i for i in self.ingredientes if i['nombre'] != nombre]

    def verificar_stock(self, menu):
        for ingrediente, cantidad_requerida in self.menus[menu]['ingredientes'].items():
            ingrediente_disponible = next((i for i in self.ingredientes if i['nombre'] == ingrediente), None)
            if not ingrediente_disponible or ingrediente_disponible['cantidad'] < cantidad_requerida:
                return False
        return True

    def descontar_ingredientes(self, menu):
        for ingrediente, cantidad_requerida in self.menus[menu]['ingredientes'].items():
            for i in self.ingredientes:
                if i['nombre'] == ingrediente:
                    i['cantidad'] -= cantidad_requerida

    def reponer_ingredientes(self, menu):
        for ingrediente, cantidad_requerida in self.menus[menu]['ingredientes'].items():
            for i in self.ingredientes:
                if i['nombre'] == ingrediente:
                    i['cantidad'] += cantidad_requerida

    def agregar_pedido(self, producto, cantidad, precio):
        self.pedido_actual.append({'producto': producto, 'cantidad': cantidad, 'precio': precio})

    def eliminar_menu(self, menu):
        self.pedido_actual = [p for p in self.pedido_actual if p['producto'] != menu]

    def generar_menus_disponibles(self):
        return [menu for menu in self.menus if self.verificar_stock(menu)]

class Gestor:
    def __init__(self):
        # Listas para almacenar los ingredientes y los pedidos
        self.ingredientes = []
        self.pedido_actual = []

    def agregar_ingrediente(self, nombre, cantidad):
        # Aquí agregas el ingrediente a la lista
        self.ingredientes.append({'nombre': nombre, 'cantidad': cantidad})

    def eliminar_ingrediente(self, nombre):
        # Lógica para eliminar el ingrediente de la lista
        self.ingredientes = [i for i in self.ingredientes if i['nombre'] != nombre]

    def agregar_pedido(self, producto, cantidad, precio):
        # Añade un producto al pedido actual
        self.pedido_actual.append({'producto': producto, 'cantidad': cantidad, 'precio': precio})

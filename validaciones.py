def validar_nombre(nombre):
    return isinstance(nombre, str) and nombre != ""

def validar_cantidad(cantidad):
    try:
        cantidad = int(cantidad)
        return cantidad > 0
    except ValueError:
        return False

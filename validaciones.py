import re

def validar_nombre_ingrediente(nombre):
    """Valida que el nombre del ingrediente contenga solo letras y espacios."""
    return re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ ]+$", nombre) is not None

def validar_cantidad(cantidad):
    """Valida que la cantidad sea un número entero positivo."""
    try:
        cantidad = int(cantidad)
        if cantidad > 0:
            return cantidad
        else:
            return None
    except ValueError:
        return None

def verificar_menu_disponible(menus, ingredientes):
    """Verifica si hay suficientes ingredientes para preparar los menús."""
    faltantes = []
    for menu, ingredientes_necesarios in menus.items():
        for ingrediente, cantidad in ingredientes_necesarios.items():
            if ingrediente not in ingredientes or ingredientes[ingrediente].cantidad < cantidad:
                faltantes.append((menu, ingrediente))
    return faltantes

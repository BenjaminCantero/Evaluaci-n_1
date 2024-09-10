import re

def validar_nombre(nombre):
    if not isinstance(nombre, str):
        return "Error: El nombre debe ser una cadena de texto."
    elif nombre.strip() == "":
        return "Error: El nombre no puede estar vacío."
    elif re.search(r'\d', nombre):
        return "Error: El nombre del ingrediente no puede contener números."
    return None  # Nombre válido, sin errores

def validar_cantidad(cantidad):
    cantidad_str = str(cantidad).strip()
    
    if cantidad_str == "":
        return "Error: La cantidad no puede estar vacía."
    
    try:
        cantidad_int = int(cantidad_str)
        if cantidad_int <= 0:
            return "Error: La cantidad debe ser mayor que cero."
        return None  # Cantidad válida, sin errores
    except ValueError:
        return "Error: La cantidad debe ser un número entero válido."

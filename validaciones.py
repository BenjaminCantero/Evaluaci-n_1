def validar_nombre(nombre):
    return nombre.isalpha() and " " in nombre

def validar_cantidad(cantidad):
    return cantidad.isdigit() and int(cantidad) > 0


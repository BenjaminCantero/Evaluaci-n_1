from interfaz import Interfaz
from controlador import Controlador

if __name__ == "__main__":
    # Crear el controlador y pasar el controlador a la interfaz
    controlador = Controlador()
    app = Interfaz(controlador)

import tkinter as tk
from view import Interfaz
from gestor import Controlador

# Verifica si el script se ejecuta directamente
if __name__ == "__main__":
    # Crea una instancia de la clase Controlador
    controlador = Controlador()

    # Crea una instancia de la clase Interfaz y pasa la instancia de controlador como argumento
    interfaz = Interfaz(controlador)

    # Inicia el bucle principal de eventos de la aplicación
    interfaz.root.mainloop()

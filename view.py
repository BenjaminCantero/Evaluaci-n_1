import customtkinter as ctk
from tkinter import ttk
import gestor
import validaciones
import utils
import models

class Interfaz:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = ctk.CTk()  # Creamos la ventana principal
        self.root.geometry("800x600")  # Tamaño de la ventana
        self.root.title("Gestión de Ingredientes y Pedidos")
        
        # Crear Tabview (Control de pestañas)
        self.tab_control = ctk.CTkTabview(self.root)
        self.tab_control.pack(expand=1, fill="both")
        
        # Crear las pestañas
        self.crear_pestana_ingredientes()
        self.crear_pestana_pedidos()

        # Iniciar el loop de la interfaz gráfica
        self.root.mainloop()

    def crear_pestana_ingredientes(self):
        # Pestaña de Ingreso de Ingredientes
        tab_ingredientes = self.tab_control.add("Ingreso de Ingredientes")

        # Frame izquierdo para los campos de ingreso de ingredientes
        frame_izquierdo = ctk.CTkFrame(tab_ingredientes)
        frame_izquierdo.pack(side="left", padx=10, pady=10, fill="y")

        # Label para nombre del ingrediente
        label_nombre = ctk.CTkLabel(frame_izquierdo, text="Nombre del Ingrediente:")
        label_nombre.pack(anchor="w", pady=5)

        # Entry para ingresar el nombre del ingrediente
        self.entry_nombre = ctk.CTkEntry(frame_izquierdo, width=150)
        self.entry_nombre.pack(anchor="w", pady=5)

        # Label para cantidad
        label_cantidad = ctk.CTkLabel(frame_izquierdo, text="Cantidad:")
        label_cantidad.pack(anchor="w", pady=5)

        # Entry para ingresar la cantidad
        self.entry_cantidad = ctk.CTkEntry(frame_izquierdo, width=150)
        self.entry_cantidad.pack(anchor="w", pady=5)

        # Botón para agregar ingrediente
        boton_ingresar = ctk.CTkButton(frame_izquierdo, text="Ingresar Ingrediente", command=self.ingresar_ingrediente)
        boton_ingresar.pack(pady=10)

        # Frame derecho para la lista de ingredientes y el botón de generar menú
        frame_derecho = ctk.CTkFrame(tab_ingredientes)
        frame_derecho.pack(side="right", padx=10, pady=10, fill="y", expand=True)

        # Botón para eliminar ingrediente
        boton_eliminar = ctk.CTkButton(frame_derecho, text="Eliminar Ingrediente", command=self.eliminar_ingrediente)
        boton_eliminar.pack(pady=10)

        # Lista (Treeview) de ingredientes
        self.treeview_ingredientes = ttk.Treeview(frame_derecho, columns=("Nombre", "Cantidad"), show="headings", height=15)
        self.treeview_ingredientes.heading("Nombre", text="Nombre")
        self.treeview_ingredientes.heading("Cantidad", text="Cantidad")
        self.treeview_ingredientes.column("Nombre", width=150, anchor="center")
        self.treeview_ingredientes.column("Cantidad", width=150, anchor="center")
        self.treeview_ingredientes.pack(pady=10, padx=10, fill="both", expand=True)

        # Botón para generar menú
        boton_generar_menu = ctk.CTkButton(frame_derecho, text="Generar Menú", command=self.generar_menu)
        boton_generar_menu.pack(pady=10)

    def crear_pestana_pedidos(self):
        # Pestaña de Pedido
        tab_pedidos = self.tab_control.add("Pedido")
        
        # Frame superior para los productos
        frame_superior = ctk.CTkFrame(tab_pedidos)
        frame_superior.pack(pady=10, padx=10)

        # Botones de productos con imágenes (puedes asignar las imágenes que desees)
        boton_papas_fritas = ctk.CTkButton(frame_superior, text="Papas Fritas", command=lambda: self.agregar_pedido("Papas Fritas", 1.5))  # Precio ejemplo
        boton_papas_fritas.grid(row=0, column=0, padx=10, pady=10)

        boton_completo = ctk.CTkButton(frame_superior, text="Completo", command=lambda: self.agregar_pedido("Completo", 2.0))
        boton_completo.grid(row=0, column=1, padx=10, pady=10)

        boton_pepsi = ctk.CTkButton(frame_superior, text="Pepsi", command=lambda: self.agregar_pedido("Pepsi", 1.0))
        boton_pepsi.grid(row=0, column=2, padx=10, pady=10)

        boton_hamburguesa = ctk.CTkButton(frame_superior, text="Hamburguesa", command=lambda: self.agregar_pedido("Hamburguesa", 2.5))
        boton_hamburguesa.grid(row=0, column=3, padx=10, pady=10)

        # Frame inferior para la lista de pedidos y botones de acción
        frame_inferior = ctk.CTkFrame(tab_pedidos)
        frame_inferior.pack(pady=10, padx=10, fill="both", expand=True)

        # Tabla de pedidos (Treeview)
        self.treeview_pedidos = ttk.Treeview(frame_inferior, columns=("Nombre del Menú", "Cantidad", "Precio Unitario"), show="headings", height=10)
        self.treeview_pedidos.heading("Nombre del Menú", text="Nombre del Menú")
        self.treeview_pedidos.heading("Cantidad", text="Cantidad")
        self.treeview_pedidos.heading("Precio Unitario", text="Precio Unitario")
        self.treeview_pedidos.column("Nombre del Menú", width=150, anchor="center")
        self.treeview_pedidos.column("Cantidad", width=80, anchor="center")
        self.treeview_pedidos.column("Precio Unitario", width=100, anchor="center")
        self.treeview_pedidos.pack(pady=10, padx=10, fill="both", expand=True)

        # Label para mostrar el total
        self.label_total = ctk.CTkLabel(frame_inferior, text="Total: $0.00")
        self.label_total.pack(anchor="e", padx=20, pady=10)

        # Botón para eliminar un menú
        boton_eliminar_menu = ctk.CTkButton(frame_inferior, text="Eliminar Menú", command=self.eliminar_menu)
        boton_eliminar_menu.pack(side="left", padx=20)

        # Botón para generar boleta
        boton_generar_boleta = ctk.CTkButton(frame_inferior, text="Generar Boleta", command=self.generar_boleta)
        boton_generar_boleta.pack(side="right", padx=20)

    def ingresar_ingrediente(self):
        nombre = self.entry_nombre.get()
        cantidad = self.entry_cantidad.get()
        if validaciones.validar_nombre(nombre) and validaciones.validar_cantidad(cantidad):
            self.controlador.agregar_ingrediente(nombre, int(cantidad))
            # Actualiza la interfaz (actualiza la Treeview, etc.)
        else:
            # Maneja errores de validación
            pass

    def eliminar_ingrediente(self):
        seleccionado = self.treeview_ingredientes.selection()
        if seleccionado:
            nombre = self.treeview_ingredientes.item(seleccionado)['values'][0]
            self.controlador.eliminar_ingrediente(nombre)
            # Actualiza la interfaz (elimina el elemento de la Treeview, etc.)

    def generar_menu(self):
        # Lógica para generar un menú (ejemplo simplificado)
        pass

    def agregar_pedido(self, nombre, precio):
        # Lógica para agregar un pedido
        pass

    def eliminar_menu(self):
        # Lógica para eliminar un menú (ejemplo simplificado)
        pass

    def generar_boleta(self):
        utils.generar_boleta(self.controlador.pedido_actual)
        # Asegúrate de que la boleta se guarda correctamente en el archivo

# Ejecución de la aplicación
if __name__ == "__main__":
    # Se cambia por la versión del constructor que acepta el controlador
    interfaz = Interfaz()

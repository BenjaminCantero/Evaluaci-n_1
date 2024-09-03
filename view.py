import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk

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

        # Ajustar las columnas en la grilla
        tab_ingredientes.grid_columnconfigure(0, weight=1)
        tab_ingredientes.grid_columnconfigure(1, weight=1)
        tab_ingredientes.grid_columnconfigure(2, weight=1)

        # Label para nombre del ingrediente
        label_nombre = ctk.CTkLabel(tab_ingredientes, text="Nombre del Ingrediente:")
        label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # Entry para ingresar el nombre del ingrediente
        self.entry_nombre = ctk.CTkEntry(tab_ingredientes, width=200)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        # Label para cantidad
        label_cantidad = ctk.CTkLabel(tab_ingredientes, text="Cantidad:")
        label_cantidad.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        # Entry para ingresar la cantidad
        self.entry_cantidad = ctk.CTkEntry(tab_ingredientes, width=200)
        self.entry_cantidad.grid(row=1, column=1, padx=10, pady=10)

        # Botón para agregar ingrediente
        boton_ingresar = ctk.CTkButton(tab_ingredientes, text="Ingresar Ingrediente", command=self.ingresar_ingrediente)
        boton_ingresar.grid(row=2, column=0, columnspan=2, pady=10)

        # Lista (Treeview) de ingredientes
        self.treeview_ingredientes = ttk.Treeview(tab_ingredientes, columns=("Nombre", "Cantidad"), show="headings", height=8)
        self.treeview_ingredientes.heading("Nombre", text="Nombre")
        self.treeview_ingredientes.heading("Cantidad", text="Cantidad")
        self.treeview_ingredientes.column("Nombre", width=200, anchor="center")
        self.treeview_ingredientes.column("Cantidad", width=100, anchor="center")
        self.treeview_ingredientes.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Botón para eliminar ingrediente
        boton_eliminar = ctk.CTkButton(tab_ingredientes, text="Eliminar Ingrediente", command=self.eliminar_ingrediente)
        boton_eliminar.grid(row=0, column=2, padx=10, pady=10, sticky="ne")

        # Botón para generar menú
        boton_generar_menu = ctk.CTkButton(tab_ingredientes, text="Generar Menú", command=self.generar_menu)
        boton_generar_menu.grid(row=4, column=1, columnspan=2, pady=10, sticky="s")

    def crear_pestana_pedidos(self):
        # Pestaña de Pedido
        tab_pedidos = self.tab_control.add("Pedido")

        # Aquí agregas la lógica para la pestaña de pedidos, como botones y visualización de menús
        label_info = ctk.CTkLabel(tab_pedidos, text="Aquí irán los pedidos.")
        label_info.pack(pady=20)

    def ingresar_ingrediente(self):
        # Obtener los valores de los campos de entrada
        nombre = self.entry_nombre.get()
        cantidad = self.entry_cantidad.get()

        # Validar las entradas (asumiendo que tienes una función de validación)
        if not nombre or not cantidad.isdigit():
            messagebox.showerror("Error", "Por favor ingresa un nombre válido y una cantidad numérica.")
            return

        # Agregar el ingrediente al controlador
        self.controlador.agregar_ingrediente(nombre, int(cantidad))

        # Actualizar la lista de ingredientes
        self.treeview_ingredientes.insert("", "end", values=(nombre, cantidad))
        
        # Limpiar las entradas
        self.entry_nombre.delete(0, 'end')
        self.entry_cantidad.delete(0, 'end')

    def eliminar_ingrediente(self):
        # Eliminar ingrediente seleccionado del Treeview
        selected_item = self.treeview_ingredientes.selection()

        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor selecciona un ingrediente para eliminar.")
            return

        # Obtener el nombre del ingrediente seleccionado
        ingrediente_nombre = self.treeview_ingredientes.item(selected_item, "values")[0]

        # Eliminar del controlador
        self.controlador.eliminar_ingrediente(ingrediente_nombre)

        # Eliminar del Treeview
        self.treeview_ingredientes.delete(selected_item)

    def generar_menu(self):
        # Implementa la lógica para generar menús
        messagebox.showinfo("Generar Menú", "Función no implementada aún")

import customtkinter as ctk
from tkinter import messagebox, ttk
from ingredientes import Ingrediente

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Ingredientes")
        self.root.geometry("1200x800")
        self.ingredientes = {}
        self.nombre_var = ctk.StringVar()
        self.cantidad_var = ctk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        # Configuración de filas y columnas
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        
        # Campos de entrada
        ctk.CTkLabel(self.root, text="Nombre del Ingrediente:").grid(row=0, column=0, pady=10, sticky="ew")
        ctk.CTkEntry(self.root, textvariable=self.nombre_var).grid(row=0, column=1, pady=10, sticky="ew")
        
        ctk.CTkLabel(self.root, text="Cantidad:").grid(row=1, column=0, pady=10, sticky="ew")
        ctk.CTkEntry(self.root, textvariable=self.cantidad_var).grid(row=1, column=1, pady=10, sticky="ew")
        
        ctk.CTkButton(self.root, text="Ingresar Ingrediente", command=self.add_ingrediente).grid(row=2, column=0, columnspan=2, pady=20)
        
        ctk.CTkButton(self.root, text="Eliminar Ingrediente", command=self.delete_ingrediente).grid(row=3, column=1, sticky='e', pady=10)
        
        # Treeview para mostrar la lista de ingredientes
        self.tree = ttk.Treeview(self.root, columns=("Nombre", "Cantidad"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.column("Nombre", width=150)
        self.tree.column("Cantidad", width=100)
        self.tree.grid(row=4, column=0, columnspan=2, pady=20, sticky="nsew")
        
        ctk.CTkButton(self.root, text="Generar Menú", command=self.generar_menu).grid(row=5, column=0, columnspan=2, pady=10)

    def add_ingrediente(self):
        from validaciones import validar_nombre_ingrediente, validar_cantidad

        nombre = self.nombre_var.get()
        cantidad = self.cantidad_var.get()
        
        if not validar_nombre_ingrediente(nombre):
            messagebox.showerror("Error de entrada", "El nombre del ingrediente debe contener solo letras y espacios.")
            return
        
        cantidad_valida = validar_cantidad(cantidad)
        if cantidad_valida is None:
            messagebox.showerror("Error de entrada", "La cantidad debe ser un número entero positivo válido.")
            return

        if nombre in self.ingredientes:
            self.ingredientes[nombre].actualizar_cantidad(cantidad_valida)
        else:
            self.ingredientes[nombre] = Ingrediente(nombre, cantidad_valida)
        self.update_treeview()
        messagebox.showinfo("Éxito", f"Ingrediente {nombre} agregado con éxito.")

    def update_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for nombre, ing in self.ingredientes.items():
            self.tree.insert("", "end", values=(nombre, ing.cantidad))

    def delete_ingrediente(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            nombre = item['values'][0]
            if nombre in self.ingredientes:
                del self.ingredientes[nombre]
                self.update_treeview()
                messagebox.showinfo("Éxito", f"Ingrediente {nombre} eliminado con éxito.")
        else:
            messagebox.showwarning("Error", "Seleccione un ingrediente para eliminar.")

    def generar_menu(self):
        from validaciones import verificar_menu_disponible

        menus = {
            "Papas fritas": {"papas": 5},
            "Pepsi": {"bebida": 1},
            "Completo": {"vienesa": 1, "pan de completo": 1, "tomate": 1, "palta": 1},
            "Hamburguesa": {"pan de hamburguesa": 1, "lámina de queso": 1, "churrasco de carne": 1}
        }
        
        faltantes = verificar_menu_disponible(menus, self.ingredientes)
        
        if faltantes:
            mensaje = "Faltan los siguientes ingredientes para generar los menús:\n"
            for menu, ingrediente in faltantes:
                mensaje += f"- {ingrediente} para {menu}\n"
            messagebox.showwarning("Advertencia", mensaje)
        else:
            messagebox.showinfo("Éxito", "Todos los menús pueden ser generados con éxito.")

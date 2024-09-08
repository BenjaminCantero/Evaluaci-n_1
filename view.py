import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk


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
        self.crear_pedidos()

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

        #boton eliminar ingrediente
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

    def crear_pedidos(self):
        tab_pedidos = self.tab_control.add("Pedido")
        
        frame_productos = ctk.CTkFrame(tab_pedidos)
        frame_productos.pack(pady=20)
        
        productos = {
            "Papas Fritas": "icons/papas_fritas.png",
            "completo": "icons/completo.png",
            "hamburguesa": "icons/hamburguesa.png",
            "pepsi": "icons/pepsi.png",
        }
        
        
        self.imagenes_productos = {}
        
        for producto, img_file in productos.items():
            try:
                pill_image = Image.open(img_file)
                imagen = ImageTk.PhotoImage(pill_image)
                self.imagenes_productos[producto] = imagen
                
                boton_productos = ctk.CTkButton(
                    frame_productos,
                    image= imagen,
                    text=producto,
                    compound="top",
                    command=lambda p=producto: self.agregar_producto(p)
                )
                boton_productos.pack(side= "left", padx= 10, pady= 10)
            except Exception as e:
                print(f"Error al cargar la imagen {img_file}: {e}")
                
        self.treeview_pedidos = ttk.Treeview(tab_pedidos, columns=("Producto", "Cantidad", "Precio Unitario"), show="headings", height=8)   
        self.treeview_pedidos.heading("Producto", text="Producto")
        self.treeview_pedidos.heading("Cantidad", text="Cantidad")
        self.treeview_pedidos.heading("Precio Unitario", text="Precio Unitario")
        self.treeview_pedidos.pack(pady=10, padx=10, fill= "both", expand=True)

        def generar_boleta(self):
            messagebox.showinfo("Generar Boleta", "Función no implementada aún")


    def ingresar_ingrediente(self):
        nombre = self.entry_nombre.get()
        cantidad = self.entry_cantidad.get()

        if not nombre or not cantidad.isdigit():
            messagebox.showerror("Error", "Por favor ingresa un nombre válido y una cantidad numérica.")
            return

        self.controlador.agregar_ingrediente(nombre, int(cantidad))
        self.treeview_ingredientes.insert("", "end", values=(nombre, cantidad))
        self.entry_nombre.delete(0, 'end')
        self.entry_cantidad.delete(0, 'end')

    def eliminar_ingrediente(self):
        selected_item = self.treeview_ingredientes.selection()

        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor selecciona un ingrediente para eliminar.")
            return

        ingrediente_nombre = self.treeview_ingredientes.item(selected_item, "values")[0]
        self.controlador.eliminar_ingrediente(ingrediente_nombre)
        self.treeview_ingredientes.delete(selected_item)

    def generar_menu(self):
        messagebox.showinfo("Generar Menú", "Función no implementada aún")

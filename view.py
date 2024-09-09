import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps


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
        
    def agregar_producto(self, producto, precio):
        for item in self.treeview_pedidos.get_children():
            values = self.treeview_pedidos.item(item, "values")
            if values[0] == producto:
                cantidad_actual = int(values[1])
                nueva_cantidad = cantidad_actual + 1
                self.treeview_pedidos.item(item, values=(producto, nueva_cantidad, precio))      
                return
            
        cantidad = 1
        self.treeview_pedidos.insert("", "end", values=(producto, cantidad, precio))
        
    def crear_pedidos(self):
        tab_pedidos = self.tab_control.add("Pedido")
        
        
        frame_productos = ctk.CTkFrame(tab_pedidos, fg_color="transparent")
        frame_productos.pack(pady=20)
        
        self.productos = {
            "Papas Fritas": ("icons/papas_fritas.png", 500),
            "completo": ("icons/completo.png", 1800),
            "hamburguesa": ("icons/hamburguesa.png", 3500),
            "pepsi": ("icons/pepsi.png", 1100),
        }
        
        
        self.imagenes_productos = {}
        for producto, (img_file, precio) in self.productos.items():
            try:
                pill_image = Image.open(img_file).convert("RGBA")
                background = Image.new('RGBA', pill_image.size, (0, 0, 0, 0))
                imagen_transparente = Image.alpha_composite(background, pill_image)               
                imagen_borde = ImageOps.expand(imagen_transparente, border=1, fill="red")
                imagen = ImageTk.PhotoImage(imagen_borde)
                
                self.imagenes_productos[producto] = imagen
            
            # Crear el botón de producto con la imagen
                boton_productos = ctk.CTkButton(
                    frame_productos,
                    image=imagen,
                    text=f"{producto}",
                    compound="top",
                    fg_color="transparent",  # Establecer color de fondo transparente
                    command=lambda p=producto, pr=precio: self.agregar_producto(p, pr),
                )
                boton_productos.pack(side="left", padx=10, pady=10)
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

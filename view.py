import customtkinter as ctk
from tkinter import messagebox
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

        # Botón eliminar ingrediente
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
	
        # Boton para generar boleta
        boton_generar_boleta = ctk.CTkButton(tab_pedidos, text="Generar boleta", command=self.generar_boleta)
        boton_generar_boleta.pack(pady=10)

        # Boton para eliminar pedido seleccionado
        boton_eliminar_seleccionado = ctk.CTkButton(tab_pedidos, text="Eliminar Pedido Seleccionado", command=self.eliminar_pedido_seleccionado)
        boton_eliminar_seleccionado.pack(pady=5)
        

    def generar_boleta(self):
        # Obtener los productos y sus cantidades del Treeview
        items = self.treeview_pedidos.get_children()
        if not items:
            messagebox.showwarning("advertencia", "no hay productos en el pedido para generar una boleta.")
            return

        boleta = "boleta de pedido:\n\n"
        total = 0

        for item in items:
            producto, cantidad, precio_unitario = self.treeview_pedidos.item(item, "values")
            cantidad = int(cantidad)
            precio_unitario = int(precio_unitario)
            subtotal = cantidad * precio_unitario
            total += subtotal
            boleta += f"{producto} x {cantidad} - ${subtotal}\n"

        boleta += f"\nTotal: ${total}"
        messagebox.showinfo("boleta de pedido", boleta)

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
    
    def eliminar_pedido_seleccionado(self):
        selected_item = self.treeview_pedidos.selection()

        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor selecciona un pedido para eliminar.")
            return

        self.treeview_pedidos.delete(selected_item)

    def generar_menu(self):
        # Diccionario de recetas predefinidas con los ingredientes necesarios
        recetas = {
            "ensalada cesar": ["lechuga", "pollo", "queso parmesano", "crutones"],
            "sandwich de jamon y queso": ["pan", "jamon", "queso", "mantequilla"],
            "tacos de carne": ["tortillas", "carne", "cebolla", "tomate"],
            "pizza margarita": ["harina", "tomate", "queso", "albahaca"],
            "hamburguesa clasica": ["pan de hamburguesa", "carne", "lechuga", "tomate", "queso"],
            "spaghetti a la boloñesa": ["spaghetti", "carne", "tomate", "cebolla", "ajo"],
        }

        # Obtener los ingredientes disponibles en el inventario
        ingredientes_disponibles = set()
        for item in self.treeview_ingredientes.get_children():
            nombre, _ = self.treeview_ingredientes.item(item, "values")
            ingredientes_disponibles.add(nombre.lower())

        if not ingredientes_disponibles:
            messagebox.showwarning("advertencia", "no hay ingredientes disponibles para generar un menu.")
            return

        # Generar menu en base a las recetas y los ingredientes disponibles
        menu = "menu generado:\n\n"
        recetas_completas = False
        
        for plato, ingredientes_necesarios in recetas.items():
            # Comprobar si todos los ingredientes necesarios estan en el inventario
            if all(ingrediente in ingredientes_disponibles for ingrediente in ingredientes_necesarios):
                recetas_completas = True
                menu += f"receta completa: {plato} - ingredientes: {', '.join(ingredientes_necesarios)}\n"

        if not recetas_completas:
            # Si no hay recetas completas mostrar recetas con al menos un ingrediente disponible
            recetas_parciales = False
            for plato, ingredientes_necesarios in recetas.items():
                if any(ingrediente in ingredientes_disponibles for ingrediente in ingredientes_necesarios):
                    recetas_parciales = True
                    menu += f"receta parcial: {plato} - ingredientes necesarios: {', '.join(ingredientes_necesarios)}\n"

            if not recetas_parciales:
                menu = "no hay ingredientes disponibles para sugerir ningun plato."

        messagebox.showinfo("menu generado", menu)

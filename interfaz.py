import customtkinter as ctk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageOps
import validaciones as val

class Interfaz:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = ctk.CTk()
        self.root.geometry("1024x600")
        self.root.title("Gestión de Ingredientes y Pedidos")
        
        # Crear Tabview (control de pestañas)
        self.tab_control = ctk.CTkTabview(self.root)
        self.tab_control.pack(expand=1, fill="both")
        
        # Crear las pestañas
        self.crear_pestana_ingredientes()
        self.crear_pedidos()

        # Lista para guardar ingredientes
        self.ingredientes_guardados = []

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

        # Frame derecho para la lista de ingredientes y los botones
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

    def crear_pedidos(self):
        tab_pedidos = self.tab_control.add("Pedido")
        
        frame_productos = ctk.CTkFrame(tab_pedidos, fg_color="transparent")
        frame_productos.pack(pady=20)
        
        # Lista de productos e imágenes
        self.productos = {
            "Papas Fritas": ("icons/papas_fritas.png", 500),
            "Completo": ("icons/completo.png", 1800),
            "Hamburguesa": ("icons/hamburguesa.png", 3500),
            "Pepsi": ("icons/pepsi.png", 1100),
        }
        self.imagenes_productos = {}
        row, column = 0, 0
        for producto, (img_file, precio) in self.productos.items():
            try:
                pill_image = Image.open(img_file).convert("RGBA")
                background = Image.new('RGBA', pill_image.size, (0, 0, 0, 0))
                imagen_transparente = Image.alpha_composite(background, pill_image)
                imagen_borde = ImageOps.expand(imagen_transparente, border=1, fill="red")
                imagen = ImageTk.PhotoImage(imagen_borde)
                
                self.imagenes_productos[producto] = imagen
                
                boton_productos = ctk.CTkButton(
                    frame_productos,
                    image=imagen,
                    text=f"{producto}",
                    compound="top",
                    fg_color="transparent",  # Fondo transparente
                    command=lambda p=producto, pr=precio: self.agregar_producto(p, pr),
                )
                boton_productos.grid(row=row, column=column, padx=10, pady=10)
                
                column += 1
                if column > 1:
                    column = 0
                    row += 1
                
            except Exception as e:
                print(f"Error al cargar la imagen {img_file}: {e}")

        # Frame para contener los botones y el total
        frame_botones = ctk.CTkFrame(tab_pedidos, fg_color="transparent")
        frame_botones.pack(pady=10, fill="x")

        # Label del monto total
        self.label_total = ctk.CTkLabel(frame_botones, text="Total: $0.00", anchor="e")
        self.label_total.pack(side="right", padx=10)              
        # Botón para eliminar menú
        boton_eliminar_pedido = ctk.CTkButton(frame_botones, text="Eliminar Menú", command=self.eliminar_pedido)
        boton_eliminar_pedido.pack(side="right", padx=10)
        self.treeview_pedidos = ttk.Treeview(tab_pedidos, columns=("Producto", "Cantidad", "Precio Unitario"), show="headings", height=8)   
        self.treeview_pedidos.heading("Producto", text="Producto")
        self.treeview_pedidos.heading("Cantidad", text="Cantidad")
        self.treeview_pedidos.heading("Precio Unitario", text="Precio Unitario")
        self.treeview_pedidos.pack(pady=10, padx=10, fill="both", expand=True)

        # Botón para generar boleta
        boton_generar_boleta = ctk.CTkButton(frame_botones, text="Generar Boleta", command=self.generar_boleta)
        boton_generar_boleta.pack(side="right", padx=10)

    def agregar_producto(self, producto, precio):
        for item in self.treeview_pedidos.get_children():
            values = self.treeview_pedidos.item(item, "values")
            if values[0] == producto:
                cantidad_actual = int(values[1])
                nueva_cantidad = cantidad_actual + 1
                nuevo_total = nueva_cantidad * precio
                self.treeview_pedidos.item(item, values=(producto, nueva_cantidad, precio, nuevo_total))
                self.actualizar_total()
                return
            
        cantidad = 1
        total = cantidad * precio
        self.treeview_pedidos.insert("", "end", values=(producto, cantidad, precio, total))
        self.actualizar_total()
    
    def eliminar_pedido(self):
        seleccionado = self.treeview_pedidos.selection()
        if seleccionado:
            self.treeview_pedidos.delete(seleccionado)
            self.actualizar_total()

    def actualizar_total(self):
        total = 0
        for item in self.treeview_pedidos.get_children():
            total += float(self.treeview_pedidos.item(item, "values")[3])
        self.label_total.configure(text=f"Total: ${total:.2f}")

    def generar_boleta(self):
        # Código para generar boleta
        pass

    def ingresar_ingrediente(self):
        nombre = self.entry_nombre.get()
        cantidad = self.entry_cantidad.get()
        
        # Validar datos
        resultado_validacion_nombre = val.validar_nombre(nombre)
        resultado_validacion_cantidad = val.validar_cantidad(cantidad)
        
        if resultado_validacion_nombre:
            messagebox.showerror("Error", resultado_validacion_nombre)
            return
        
        if resultado_validacion_cantidad:
            messagebox.showerror("Error", resultado_validacion_cantidad)
            return
        
        # Verificar si el ingrediente ya está en la lista
        for item in self.treeview_ingredientes.get_children():
            values = self.treeview_ingredientes.item(item, "values")
            if values[0] == nombre:
                messagebox.showwarning("Advertencia", "El ingrediente ya está en la lista.")
                return
        
        # Si no hay errores, continuar con el ingreso del ingrediente
        self.treeview_ingredientes.insert("", "end", values=(nombre, cantidad))

    def eliminar_ingrediente(self):
        seleccionado = self.treeview_ingredientes.selection()
        if seleccionado:
            self.treeview_ingredientes.delete(seleccionado)
    
    def generar_menu(self):
        # Recuperar todos los ingredientes de la lista
        ingredientes = []
        for item in self.treeview_ingredientes.get_children():
            values = self.treeview_ingredientes.item(item, "values")
            nombre = values[0]
            cantidad = values[1]
            ingredientes.append((nombre, cantidad))
        
        # Verificar si hay ingredientes
        if not ingredientes:
            messagebox.showerror("Error", "No hay ingredientes disponibles para generar el menú.")
            return
        
        # Guardar los ingredientes para usarlos posteriormente
        self.ingredientes_guardados = ingredientes
        
        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Ingredientes guardados en la lista de ingredientes guardados.")

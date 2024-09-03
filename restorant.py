import customtkinter as ctk
import tkinter as tk

class Aplicacion(ctk.CTk):
    def __init__(self, root):
        super().__init__()

        self.title("Restaurant")
        self.geometry("800x600")

        
        self.tabview = ctk.CTkTabview(self, width=600, height=500)
        self.tabview.pack(pady=20, padx=20, fill="both", expand=True)

        # Creación de pestañas
        self.crear_pestana()

    def crear_pestana(self):
        
        tab_menu = self.tabview.add("Menú")
        
        
        label_menu = ctk.CTkLabel(tab_menu, text="Bienvenido al Menú")
        label_menu.pack(pady=20, padx=20)
        
        boton_agregar_menu = ctk.CTkButton(tab_menu, text="Agregar menu", command=self.agregar_menu)
        boton_agregar_menu.pack(pady=10)
        
        boton_eliminar_menu = ctk.CTkButton(tab_menu, text="Eliminar menu", command=self.eliminar_menu)
        boton_eliminar_menu.pack(pady=10)
        
        self.lista_menus = ctk.CTkTextbox(tab_menu, width=400, height=200)
        self.lista_menus.pack(pady=10)
        self.lista_menus.insert("end", "menu disponible: Papas fritas, pepsi, completo, hambirguesa")
        
    def agregar_menu(self):
        self.lista_menus.insert("end", "\nNuevo menu añadido") 
    
    def eliminar_menu(self):
        self.lista_menus.delete("1.0", "end")       

root = tk.Tk()


app = Aplicacion(root)
root.mainloop()

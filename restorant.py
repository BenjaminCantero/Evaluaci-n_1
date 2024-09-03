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


root = tk.Tk()


app = Aplicacion(root)
root.mainloop()

import customtkinter as ctk
from tkinter import ttk

def crear_pedido(tab_control1):
    tab_pedidos = tab_control1.ADD("Pedido")
    
    
    label_info = ctk.CTkLabel(tab_pedidos, text= "aqui iran los pedidos")
    label_info.pack(pady=20)
    
    
    return tab_pedidos
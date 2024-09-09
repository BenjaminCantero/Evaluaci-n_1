from tkinter import messagebox

def generar_boleta(pedido_actual):
    total_general = sum([item['cantidad'] * item['precio'] for item in pedido_actual])
    contenido_boleta = "\n".join([f"{item['producto']} x{item['cantidad']} = {item['precio']*item['cantidad']}" for item in pedido_actual])
    contenido_boleta += f"\nTotal: {total_general}"
    messagebox.showinfo("Boleta", contenido_boleta)

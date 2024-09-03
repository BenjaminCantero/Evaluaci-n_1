import customtkinter as ctk
from fpdf import FPDF

#clase para manejar la generacion de boletas
class Boleta:
    def __init__(self, cliente, producto, cantidad, precio_unitario ):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad 
        self.precio_unitario = precio_unitario
        self.total = cantidad = precio_unitario

# Método para generar el PDF de la boleta
    def generar_pdf(self, filename="boleta.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        pdf.cell(200, 10, txt="Boleta de Compra", ln=True, align="C")
        pdf.ln(10)
        
        pdf.cell(100, 10, txt=f"Cliente: {self.cliente}", ln=True)
        pdf.cell(100, 10, txt=f"Producto: {self.producto}", ln=True)
        pdf.cell(100, 10, txt=f"Cantidad: {self.cantidad}", ln=True)
        pdf.cell(100, 10, txt=f"Precio Unitario: S/ {self.precio_unitario:.2f}", ln=True)
        pdf.cell(100, 10, txt=f"Total: S/ {self.total:.2f}", ln=True)
        
        pdf.output(filename)
        print(f"Boleta generada y guardada como {filename}")

#Clase para manejar la interfaz grafica
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Generador de Boleta")
        self.geometry("400X400")

        #variables de la interfaz
        self.cliente_var = ctk.StringVar()
        self.producto_var = ctk.StringVar()
        self.cantidad_var = ctk.StringVar()
        self.precio_unitario_var = ctk.StringVar()

        #componentes de la interfaz
        ctk.CTkLabel(self, text="Cliente:").pack(pady=10)
        self.cliente_entry = ctk.CTkEntry(self, textvariable=self.cliente_var)
        self.cliente_entry.pack(pady=10)

        ctk.CTkLabel(self, text="Producto:").pack(pady=10)
        self.producto_entry = ctk.CTkEntry(self, textvariable=self.producto_var)
        self.producto_entry.pack(pady=10)

        ctk.CTkLabel(self, text="Cantidad:").pack(pady=10)
        self.cantidad_entry = ctk.CTkEntry(self, textvariable=self.cantidad_var)
        self.cantidad_entry.pack(pady=10)

        ctk.CTkLabel(self, text="Precio Unitario:").pack(pady=10)
        self.precio_unitario_entry = ctk.CTkEntry(self, textvariable=self.precio_unitario_var)
        self.precio_unitario_entry.pack(pady=10)

        self.generar_button = ctk.CTkButton(self, text="Generar Boleta", command=self.generar_boleta)
        self.generar_button.pack(pady=20)

        
    #metodo para generar la boleta y guardarla como pdf
    def generar_boleta(self):
        cliente = self.cliente_var.get()
        producto = self.producto_var.get()
        cantidad = int(self.cantidad_var.get())
        precio_unitario = float(self.precio_unitario_var.get())

        #crear una instancia de ;a clase boleta
        boleta = Boleta(cliente, producto, cantidad, precio_unitario)

        #generar el pdf de la boleta
        boleta.generar_pdf()

#ejecutar la apliocacion
if __name__ == "__main__":
    app = App()
    app.mainloop()

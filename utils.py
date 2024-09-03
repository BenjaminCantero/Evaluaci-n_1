from fpdf import FPDF

def generar_boleta(pedido):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Boleta de Compra", ln=True, align="C")
    
    for menu in pedido.menus:
        pdf.cell(200, 10, txt=f"{menu.nombre}: {menu.precio}", ln=True)
    
    pdf.cell(200, 10, txt=f"Total: {pedido.total}", ln=True)
    pdf.output("boleta.pdf")

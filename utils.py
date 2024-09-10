from fpdf import FPDF
from datetime import datetime

def generar_boleta(pedido_actual):
    # Crear instancia de FPDF
    pdf = FPDF()
    pdf.add_page()

    # Establecer el título
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Boleta Restaurante", ln=True, align='L')  # Texto alineado a la izquierda

    # Información del restaurante (alineado a la izquierda)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, "Razón Social del Negocio", ln=True, align='L')
    pdf.cell(0, 10, "RUT: 12345678-9", ln=True, align='L')
    pdf.cell(0, 10, "Dirección: Calle Falsa 123", ln=True, align='L')
    pdf.cell(0, 10, "Teléfono: +56 9 1234 5678", ln=True, align='L')

    # Fecha y hora (alineado a la derecha)
    fecha_actual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    pdf.cell(0, 10, f"Fecha: {fecha_actual}", ln=True, align='R')  # Texto alineado a la derecha

    # Espacio antes de los detalles del pedido
    pdf.ln(10)

    # Título de la tabla
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(90, 10, "Producto", 1)
    pdf.cell(30, 10, "Cantidad", 1)
    pdf.cell(40, 10, "Precio Unitario", 1)
    pdf.cell(40, 10, "Subtotal", 1)
    pdf.ln(10)

    # Detalles del pedido
    pdf.set_font("Arial", '', 12)
    for item in pedido_actual["items"]:
        nombre, cantidad, precio_unitario, subtotal = item
        pdf.cell(90, 10, nombre, 1)
        pdf.cell(30, 10, str(cantidad), 1)
        pdf.cell(40, 10, f"${precio_unitario:.2f}", 1)
        pdf.cell(40, 10, f"${subtotal:.2f}", 1)
        pdf.ln(10)

    # Calcular Subtotal, IVA, y Total
    total = pedido_actual['total']
    iva = total * 0.19
    total_con_iva = total + iva

    # Espacio antes de los totales
    pdf.ln(10)

    # Mostrar Subtotal
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(160, 10, "Subtotal:", 0, 0, 'R')
    pdf.cell(40, 10, f"${total:.2f}", 0, ln=True, align='R')

    # Mostrar IVA
    pdf.cell(160, 10, "IVA (19%):", 0, 0, 'R')
    pdf.cell(40, 10, f"${iva:.2f}", 0, ln=True, align='R')

    # Mostrar Total
    pdf.cell(160, 10, "Total:", 0, 0, 'R')
    pdf.cell(40, 10, f"${total_con_iva:.2f}", 0, ln=True, align='R')

    # Espacio para el mensaje final
    pdf.ln(20)
    pdf.set_font("Arial", 'I', 12)

    # Mensaje centrado en la parte de abajo
    pdf.cell(0, 10, "Gracias por su compra.Para cualquier consulta, llámenos al +569 12345678", ln=True, align='C')
    
    # Mensaje adicional: "Los productos adquiridos no tienen garantía"
    pdf.cell(0, 10, "Los productos adquiridos no tienen garantía", ln=True, align='C')

    # Guardar el PDF
    pdf.output("boleta.pdf")
    print("Boleta generada con éxito.")

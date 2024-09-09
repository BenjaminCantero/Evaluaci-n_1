from PIL import Image, ImageTk

def test_image_loading():
    try:
        img = Image.open("icons/papas_fritas.png")
        img.show()  # Esto debería abrir la imagen en el visor predeterminado
    except Exception as e:
        print(f"Error al abrir la imagen de prueba: {e}")

test_image_loading()

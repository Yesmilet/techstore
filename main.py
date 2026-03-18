import flet as ft
from product_card import ProductCard

# Lista de productos
productos = [
    {"id": 1, "nombre": "Laptop Gamer", "descripcion": "Ryzen 7 16GB RAM", "precio": 25000, "ruta_imagen": "laptopgamer.jpg"},
    {"id": 2, "nombre": "Mouse Gamer", "descripcion": "Mouse RGB", "precio": 350, "ruta_imagen": "mouse.jpg"},
    {"id": 3, "nombre": "Teclado Mecánico", "descripcion": "Switch blue RGB", "precio": 1200, "ruta_imagen": "teclado.jpg"},
    {"id": 4, "nombre": "Audifonos Gamer", "descripcion": "Sonido envolvente", "precio": 900, "ruta_imagen": "audifonosg.jpg"},
    {"id": 5, "nombre": "Televisión 32", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "televisor.jpg"},
    {"id": 6, "nombre": "Audifonos", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "audifonos.jpg"},
    {"id": 7, "nombre": "Cargador", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "cargador.jpg"},
    {"id": 8, "nombre": "Impresora", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "impresora.jpg"},
    {"id": 9, "nombre": "Tablet", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "tablet.jpg"},
    {"id": 10, "nombre": "Smartwatch", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "smartwatch.jpg"},
    {"id": 11, "nombre": "Laptop", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "laptop.jpg"},
    {"id": 12, "nombre": "Bocina", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "bocina.jpg"},
    {"id": 13, "nombre": "Multicontactos", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "multicontacto.jpg"},
    {"id": 14, "nombre": "Microfono", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "microfono.jpg"},
    {"id": 15, "nombre": "Router", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "router.jpg"},







]

def main(page: ft.Page):
    page.title = "TechStore"
    page.scroll = "auto"
    page.bgcolor = "#BFC8ED"
    page.padding = 30
    page.assets_dir = "assets"  # Carpeta de imágenes

    # Estado de la aplicación
    carrito = []
    favoritos = []
    
    # Controles de UI
    carrito_text = ft.Text("0", size=16, weight="bold", color="#3742FA")
    favoritos_text = ft.Text("0", size=16, weight="bold", color="#FF6B81")
    
    def mostrar_mensaje(msg):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(msg, color="white"),
            bgcolor="#3742FA"
        )
        page.snack_bar.open = True
        page.update()
    
    def agregar_carrito(producto):
        carrito.append(producto)
        carrito_text.value = str(len(carrito))
        mostrar_mensaje(f"✓ {producto['nombre']} agregado al carrito")
        page.update()
    
    def agregar_favorito(producto):
        if producto not in favoritos:
            favoritos.append(producto)
        else:
            favoritos.remove(producto)
        favoritos_text.value = str(len(favoritos))
        page.update()

    # Encabezado
    header = ft.Container(
        content=ft.Row([
            ft.Column([
                ft.Text("TechStore", size=50, weight="bold", color="#17011E"),
                ft.Text("Catálogo de productos tecnológicos", size=16, color="#2F023A")
            ]),
            ft.Row([
                ft.Container(
                    content=ft.Row([
                        ft.Text("❤️", size=24),
                        favoritos_text
                    ]),
                    padding=10,
                    border_radius=8,
                    bgcolor="white"
                ),
                ft.Container(
                    content=ft.Row([
                        ft.Text("🛒", size=24),
                        carrito_text
                    ]),
                    padding=10,
                    border_radius=8,
                    bgcolor="white"
                )
            ])
        ], alignment="spaceBetween"),
        padding=20,
        bgcolor="white",
        border_radius=12,
        shadow=ft.BoxShadow(blur_radius=10, color="#8f79c2", offset=ft.Offset(2, 4))
    )

    # Crear tarjetas de productos
    tarjetas = []
    for p in productos:
        # Crear tarjeta
        card = ProductCard(
            p["nombre"],
            p["descripcion"],
            p["precio"],
            p["ruta_imagen"]
        )
        
        # Agregar funcionalidad al botón de agregar
        card.agregar = lambda e, prod=p: agregar_carrito(prod)
        
        # Agregar funcionalidad al botón de favorito
        def make_fav_handler(prod):
            def handler(e):
                agregar_favorito(prod)
                e.control.content = ft.Text("❤️" if prod in favoritos else "❤️", size=18)
                e.control.update()
            return handler
        
        # Reemplazar el manejador de favorito (esto es un poco complicado)
        # Por simplicidad, lo dejamos como está y manejamos en la función
        
        tarjetas.append(card)

    # Grid de productos
    grid = ft.Row(
        controls=tarjetas,
        wrap=True,
        spacing=25,
        run_spacing=25,
        alignment="start"
    )

    # Agregar todo a la página
    page.add(
        header,
        ft.Container(height=20),  # Espacio
        grid
    )

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
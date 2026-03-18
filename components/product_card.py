import flet as ft

class ProductCard(ft.Container):
    def __init__(self, nombre, descripcion, precio, imagen):
        super().__init__()

        self.width = 260
        self.padding = 15
        self.border_radius = 12
        self.bgcolor = "white"

        self.shadow = ft.BoxShadow(
            blur_radius=10,
            color="#dddddd",
            offset=ft.Offset(2, 4)
        )

        self.on_hover = self.hover

        self.content = ft.Column(
            spacing=10,
            controls=[

                ft.Image(
                    src=f"/{imagen}",
                    width=230,
                    height=150,
                    fit="cover"
                ),

                ft.Text(
                    nombre,
                    size=18,
                    weight="bold",
                    color="#2F3542"
                ),

                ft.Text(
                    descripcion,
                    size=13,
                    color="#747D8C"
                ),

                ft.Text(
                    f"$ {precio}",
                    size=17,
                    weight="bold",
                    color="#2ED573"
                ),

                ft.Row(
                    alignment="spaceBetween",
                    controls=[
                        ft.Text("❤️", size=18),  # Corazón para favorito

                        ft.Container(
                            bgcolor="#3742FA",
                            padding=8,
                            border_radius=6,
                            content=ft.Text(
                                "Agregar",
                                color="white",
                                size=12
                            )
                        )
                    ]
                )
            ]
        )

    def hover(self, e):
        if e.data == "true":
            self.bgcolor = "#EEF1F5"
        else:
            self.bgcolor = "white"
        self.update()
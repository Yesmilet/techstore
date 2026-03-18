#  TechStore - Proyecto Integrador (Flet + Web)

##  Descripción

Este proyecto consiste en el desarrollo de un catálogo de productos tecnológicos utilizando **Flet**, aplicando el uso de componentes reutilizables y posteriormente adaptado para despliegue web.

El sistema muestra productos en forma de tarjetas (cards), permitiendo una interfaz moderna, organizada y escalable.

---

#  Explicación del Código

##  1. Archivo principal: `main.py`

###  Importaciones

```python
import flet as ft
from product_card import ProductCard
```

* Se importa la librería Flet para la interfaz.
* Se importa la clase personalizada `ProductCard`.

---

##  2. Modelo de Datos

```python
productos = [
    {"id": 1, "nombre": "Laptop Gamer", "descripcion": "Ryzen 7 16GB RAM", "precio": 25000, "ruta_imagen": "laptopgamer.jpg"},
]
```

Se define una lista de diccionarios donde cada producto contiene:

* `id`: identificador único
* `nombre`: nombre del producto
* `descripcion`: detalles
* `precio`: valor numérico
* `ruta_imagen`: imagen en carpeta assets

 Esto permite reutilizar datos fácilmente.

---

##  3. Función principal `main(page)`

```python
def main(page: ft.Page):
```

Esta función controla toda la interfaz.

### Configuración de la página:

```python
page.title = "TechStore"
page.scroll = "auto"
page.bgcolor = "#BFC8ED"
page.assets_dir = "assets"
```

* Define título
* Activa scroll
* Color de fondo
* Ruta de imágenes

---

##  4. Creación de tarjetas

```python
for p in productos:
    card = ProductCard(
        p["nombre"],
        p["descripcion"],
        p["precio"],
        p["ruta_imagen"]
    )
```

Aquí se usa el componente reutilizable para cada producto.

 Esto evita repetir código (principio clave del proyecto).

---

##  5. Layout (Diseño)

```python
grid = ft.Row(
    controls=tarjetas,
    wrap=True,
    spacing=25
)
```

* Organiza productos en filas
* `wrap=True` permite que bajen automáticamente
* Se adapta al tamaño de pantalla

---

##  6. Ejecución

```python
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
```

Inicia la aplicación Flet.

---

#  2. Componente Reutilizable: `product_card.py`

##  Definición de clase

```python
class ProductCard(ft.Container):
```

Se crea un componente personalizado heredando de `Container`.

 Esto cumple el requisito de **herencia**.

---

##  Diseño del contenedor

```python
self.width = 260
self.padding = 15
self.border_radius = 12
self.bgcolor = "white"
```

* Tamaño fijo
* Bordes redondeados
* Fondo blanco

---

##  Sombra

```python
self.shadow = ft.BoxShadow(
    blur_radius=10,
    color="#dddddd",
    offset=ft.Offset(2, 4)
)
```

Da efecto moderno tipo tarjeta.

---

##  Imagen

```python
ft.Image(
    src=f"/{imagen}",
    width=230,
    height=150,
    fit="cover"
)
```

Carga imágenes desde `/assets`.

---

##  Textos

```python
ft.Text(nombre, size=18, weight="bold")
ft.Text(descripcion, size=13)
ft.Text(f"$ {precio}", color="#2ED573")
```

* Nombre en negritas
* Descripción pequeña
* Precio resaltado en verde

---

##  Botones

```python
ft.Row(
    controls=[
        ft.Text("❤️"),
        ft.Container(
            content=ft.Text("Agregar")
        )
    ]
)
```

* ❤️ Favorito (visual)
* 🛒 Botón agregar

---

##  Animación (Hover)

```python
self.on_hover = self.hover
```

```python
def hover(self, e):
    if e.data == "true":
        self.bgcolor = "#EEF1F5"
```

 Cambia color al pasar el mouse.

---

#  Estructura del Proyecto

```bash
PIntegrador/
│
├── main.py
├── product_card.py
├── assets/
│   ├── laptopgamer.jpg
│   ├── mouse.jpg
│   └── ...
```

---

#  Cómo ejecutar (Git Bash)

##  1. Ir al proyecto

```bash
cd C:\Users\lunaz\Downloads\TAP\PIntegrador
```

##  2. Ejecutar

```bash
python main.py
```

O en web:

```bash
flet run main.py --web
```

---

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/8492a4af-3606-4f6a-aece-8cfa42faff14" />


#  Build para Web

```bash
flet build web
```

Luego:

```bash
cd build/web
python -m http.server 8000
```

Abrir:

```
http://localhost:8000
```

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/d73b8d50-debe-473f-8835-3961dd9c5e24" />


graceful-crepe-82e897
# LINK DESPLIEGUE WEB
## https://graceful-crepe-82e897.netlify.app

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/806c8653-26d3-4e68-b5b6-21f70df50db9" />


---

#  Subir a GitHub

```bash
git init
git add .
git commit -m "Proyecto TechStore"
git branch -M main
git remote add origin https://github.com/tu-usuario/techstore.git
git push -u origin main
```

---

#  Conclusión

Este proyecto permitió:

* Aplicar herencia en componentes
* Crear interfaces reutilizables
* Manejar recursos (assets)
* Preparar una app escalable a futuro

---



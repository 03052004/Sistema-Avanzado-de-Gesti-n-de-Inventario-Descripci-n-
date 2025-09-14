# Clase Producto para representar un ítem del inventario
class Producto:

    # Constructor que inicializa los atributos del producto
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto     # ID único del producto
        self.nombre = nombre      # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible
        self.precio = precio      # Precio unitario

    # Método para actualizar la cantidad con validación
    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:  # Evitamos valores negativos
            raise ValueError("La cantidad no puede ser negativa")
        self.cantidad = nueva_cantidad  # Se actualiza la cantidad

    # Método para actualizar el precio con validación
    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio < 0:  # Evitamos precios negativos
            raise ValueError("El precio no puede ser negativo")
        self.precio = nuevo_precio  # Se actualiza el precio

    # Método especial para mostrar el producto en consola
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

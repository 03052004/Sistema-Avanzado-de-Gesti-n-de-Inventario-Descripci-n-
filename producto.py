# Definimos la clase Producto para representar un ítem del inventario
class Producto:

    # Método constructor que inicializa los atributos del producto
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en inventario
        self.precio = precio  # Precio unitario del producto

    # Método para actualizar la cantidad del producto
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad  # Asigna la nueva cantidad al atributo

    # Método para actualizar el precio del producto
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio  # Asigna el nuevo precio al atributo

    # Método especial que define cómo se muestra el producto como texto
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"  # Devuelve una cadena con los detalles del producto

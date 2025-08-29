# Importamos la clase Producto para usarla dentro del inventario
from producto import Producto


# Definimos la clase Inventario para gestionar múltiples productos
class Inventario:

    # Constructor que inicializa el diccionario de productos
    def __init__(self):
        self.productos = {}  # Diccionario con ID como clave y objetos Producto como valor

    # Método para agregar un nuevo producto al inventario
    def agregar_producto(self, producto):
        if producto.id in self.productos:  # Verifica si el ID ya existe
            print("❌ El producto ya existe.")  # Mensaje si el producto ya está registrado
        else:
            self.productos[producto.id] = producto  # Agrega el producto al diccionario

    # Método para eliminar un producto por su ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:  # Verifica si el ID existe
            del self.productos[id_producto]  # Elimina el producto del diccionario
        else:
            print("❌ Producto no encontrado.")  # Mensaje si el producto no existe

    # Método para actualizar cantidad y/o precio de un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self.productos.get(id_producto)  # Obtiene el producto por ID
        if producto:  # Si el producto existe
            if cantidad is not None:  # Si se proporciona nueva cantidad
                producto.actualizar_cantidad(cantidad)  # Actualiza cantidad
            if precio is not None:  # Si se proporciona nuevo precio
                producto.actualizar_precio(precio)  # Actualiza precio
        else:
            print("❌ Producto no encontrado.")  # Mensaje si el producto no existe

    # Método para buscar productos por nombre
    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos.values() if
                p.nombre.lower() == nombre.lower()]  # Devuelve lista de productos que coinciden con el nombre

    # Método para mostrar todos los productos del inventario
    def mostrar_todos(self):
        for producto in self.productos.values():  # Itera sobre todos los productos
            print(producto)  # Muestra cada producto usando su método __str__

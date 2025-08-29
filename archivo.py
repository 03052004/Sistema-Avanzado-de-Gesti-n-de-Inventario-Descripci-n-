# Importamos el módulo json para serializar y deserializar datos
import json

# Función para guardar el inventario en un archivo JSON
def guardar_inventario(inventario, archivo):
    datos = {
        id: {
            "nombre": p.nombre,       # Nombre del producto
            "cantidad": p.cantidad,   # Cantidad del producto
            "precio": p.precio        # Precio del producto
        } for id, p in inventario.productos.items()  # Recorremos el diccionario de productos
    }
    with open(archivo, "w") as f:  # Abrimos el archivo en modo escritura
        json.dump(datos, f)        # Guardamos los datos en formato JSON

# Función para cargar el inventario desde un archivo JSON
def cargar_inventario(archivo, clase_inventario, clase_producto):
    inventario = clase_inventario()  # Creamos una nueva instancia de Inventario
    try:
        with open(archivo, "r") as f:  # Intentamos abrir el archivo en modo lectura
            datos = json.load(f)       # Cargamos los datos desde el archivo
            for id, info in datos.items():  # Iteramos sobre cada producto guardado
                producto = clase_producto(id, info["nombre"], info["cantidad"], info["precio"])  # Creamos el objeto Producto
                inventario.agregar_producto(producto)  # Lo agregamos al inventario
    except FileNotFoundError:  # Si el archivo no existe
        pass  # No hacemos nada, simplemente devolvemos un inventario vacío
    return inventario  # Devolvemos el inventario cargado

from producto import Producto  # Importamos la clase Producto

# Clase Inventario con persistencia en archivo de texto
class Inventario:

    def __init__(self, archivo="inventario.txt"):
        self.productos = {}         # Diccionario {id: Producto}
        self.archivo = archivo      # Nombre del archivo donde se guarda el inventario
        self.cargar_desde_archivo() # Al iniciar, intentamos cargar los productos desde el archivo

    # Método para añadir un producto
    def agregar_producto(self, producto):
        if producto.id in self.productos:  # Verifica si ya existe
            print("❌ El producto ya existe.")
        else:
            self.productos[producto.id] = producto  # Se agrega al diccionario
            self.guardar_en_archivo()              # Se refleja en el archivo
            print(f"✅ Producto '{producto.nombre}' añadido correctamente.")

    # Método para eliminar un producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:           # Si existe el ID
            eliminado = self.productos[id_producto].nombre
            del self.productos[id_producto]         # Se borra del diccionario
            self.guardar_en_archivo()               # Se actualiza el archivo
            print(f"✅ Producto '{eliminado}' eliminado del inventario.")
        else:
            print("❌ Producto no encontrado.")

    # Método para actualizar un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self.productos.get(id_producto)  # Se busca el producto
        if producto:
            try:
                if cantidad is not None:           # Si se pasa cantidad
                    producto.actualizar_cantidad(cantidad)
                if precio is not None:             # Si se pasa precio
                    producto.actualizar_precio(precio)
                self.guardar_en_archivo()          # Guardamos cambios en archivo
                print(f"✅ Producto '{producto.nombre}' actualizado correctamente.")
            except ValueError as e:                # Captura errores de validación
                print(f"⚠️ Error al actualizar: {e}")
        else:
            print("❌ Producto no encontrado.")

    # Método para buscar productos por nombre
    def buscar_por_nombre(self, nombre):
        # Retorna lista de coincidencias (case-insensitive)
        return [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]

    # Mostrar todos los productos del inventario
    def mostrar_todos(self):
        if not self.productos:  # Si el inventario está vacío
            print("📦 Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    # Guardar inventario en un archivo de texto
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos.values():
                    # Se guarda cada producto en formato CSV
                    f.write(f"{p.id},{p.nombre},{p.cantidad},{p.precio}\n")
        except PermissionError:  # Si no hay permisos de escritura
            print("❌ No se tienen permisos para escribir en el archivo.")
        except Exception as e:   # Cualquier otro error inesperado
            print(f"⚠️ Error al guardar el archivo: {e}")

    # Cargar inventario desde archivo de texto
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split(",")  # Separar por comas
                    if len(partes) == 4:               # Validamos 4 campos
                        id_producto, nombre, cantidad, precio = partes
                        self.productos[id_producto] = Producto(
                            id_producto, nombre, int(cantidad), float(precio)
                        )
        except FileNotFoundError:
            # Si el archivo no existe, se notifica pero no se rompe el programa
            print("📄 No se encontró el archivo, se creará uno nuevo al guardar.")
        except PermissionError:
            print("❌ No se tienen permisos para leer el archivo.")
        except Exception as e:
            print(f"⚠️ Error al leer el archivo: {e}")

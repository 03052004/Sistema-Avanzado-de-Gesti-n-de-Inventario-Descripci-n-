# Importamos la clase Producto desde el módulo producto.py
from producto import Producto

# Importamos la clase Inventario desde el módulo inventario.py
from inventario import Inventario

# Importamos las funciones de persistencia desde archivo.py
from archivo import guardar_inventario, cargar_inventario

# Definimos la función principal que contiene el menú interactivo
def menu():
    # Cargamos el inventario desde el archivo JSON al iniciar el programa
    inventario = cargar_inventario("inventario.json", Inventario, Producto)

    # Bucle infinito para mostrar el menú hasta que el usuario decida salir
    while True:
        # Mostramos las opciones disponibles en el menú
        print("\n📋 MENÚ DE INVENTARIO")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar por nombre")
        print("5. Mostrar todos")
        print("6. Guardar y salir")

        # Solicitamos al usuario que seleccione una opción
        opcion = input("Selecciona una opción: ")

        # Opción 1: Añadir un nuevo producto al inventario
        if opcion == "1":
            id = input("ID: ")                          # Solicitamos el ID del producto
            nombre = input("Nombre: ")                  # Solicitamos el nombre
            cantidad = int(input("Cantidad: "))         # Solicitamos la cantidad (convertimos a entero)
            precio = float(input("Precio: "))           # Solicitamos el precio (convertimos a flotante)
            producto = Producto(id, nombre, cantidad, precio)  # Creamos el objeto Producto
            inventario.agregar_producto(producto)       # Lo agregamos al inventario

        # Opción 2: Eliminar un producto por su ID
        elif opcion == "2":
            id = input("ID del producto a eliminar: ")  # Solicitamos el ID
            inventario.eliminar_producto(id)            # Eliminamos el producto del inventario

        # Opción 3: Actualizar cantidad o precio de un producto
        elif opcion == "3":
            id = input("ID del producto a actualizar: ")  # Solicitamos el ID
            cantidad = input("Nueva cantidad (Enter para omitir): ")  # Cantidad opcional
            precio = input("Nuevo precio (Enter para omitir): ")      # Precio opcional
            inventario.actualizar_producto(
                id,
                int(cantidad) if cantidad else None,     # Convertimos a entero si se ingresó cantidad
                float(precio) if precio else None         # Convertimos a flotante si se ingresó precio
            )

        # Opción 4: Buscar productos por nombre
        elif opcion == "4":
            nombre = input("Nombre del producto: ")       # Solicitamos el nombre
            resultados = inventario.buscar_por_nombre(nombre)  # Buscamos coincidencias
            for p in resultados:                          # Iteramos sobre los resultados
                print(p)                                  # Mostramos cada producto encontrado

        # Opción 5: Mostrar todos los productos del inventario
        elif opcion == "5":
            inventario.mostrar_todos()                    # Llamamos al método para mostrar todos

        # Opción 6: Guardar el inventario y salir del programa
        elif opcion == "6":
            guardar_inventario(inventario, "inventario.json")  # Guardamos el inventario en el archivo
            print("✅ Inventario guardado. ¡Hasta luego!")      # Mensaje de despedida
            break                                               # Salimos del bucle y del programa

        # Si la opción ingresada no es válida
        else:
            print("❌ Opción inválida.")                   # Mensaje de error

# Punto de entrada del programa: ejecuta el menú si se corre directamente
if __name__ == "__main__":
    menu()  # Llamamos a la función del menú principal

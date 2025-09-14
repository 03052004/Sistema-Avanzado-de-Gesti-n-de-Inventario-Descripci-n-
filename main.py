from producto import Producto      # Importamos la clase Producto
from inventario import Inventario  # Importamos la clase Inventario

# Función principal con el menú interactivo
def menu():
    inventario = Inventario("inventario.txt")  # Se carga el inventario desde archivo al iniciar

    while True:
        # Mostramos las opciones
        print("\n📋 MENÚ DE INVENTARIO")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar por nombre")
        print("5. Mostrar todos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        # Opción 1: Añadir producto
        if opcion == "1":
            try:
                id = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))   # Convertimos a entero
                precio = float(input("Precio: "))     # Convertimos a flotante
                producto = Producto(id, nombre, cantidad, precio)
                inventario.agregar_producto(producto) # Se agrega y se guarda en archivo
            except ValueError:  # Captura si el usuario escribe mal cantidad/precio
                print("❌ Error: cantidad y precio deben ser numéricos.")

        # Opción 2: Eliminar producto
        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        # Opción 3: Actualizar producto
        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")
            inventario.actualizar_producto(
                id,
                int(cantidad) if cantidad else None,  # Se actualiza solo si se ingresó valor
                float(precio) if precio else None
            )

        # Opción 4: Buscar producto por nombre
        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)  # Muestra los productos encontrados
            else:
                print("❌ No se encontraron productos con ese nombre.")

        # Opción 5: Mostrar todos los productos
        elif opcion == "5":
            inventario.mostrar_todos()

        # Opción 6: Salir del programa
        elif opcion == "6":
            print("✅ Cambios guardados en inventario.txt. ¡Hasta luego!")
            break

        # Opción inválida
        else:
            print("❌ Opción inválida.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()  # Ejecuta el menú

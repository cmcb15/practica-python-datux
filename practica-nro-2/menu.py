# PRACTICA NRO 2
#  DEFINA EL SIGUIENTE DICCIONARIO
ventas=[
    {
        "fecha":"12-01-2023",
        "producto":"Producto_A",
        "cantidad":50,
        "precio":45.00,
        "promocion":True
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_AX",
        "cantidad":160,
        "precio":12.00,
        "promocion":False
    },
    {
        "fecha":"10-01-2023",
        "producto":"Producto_D",
        "cantidad":20,
        "precio":15.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_C",
        "cantidad":10,
        "precio":140.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_D",
        "cantidad":1200,
        "precio":1.00,
        "promocion":True
    }
]

def mostrar_ventas():
    print("Listado de Ventas:")
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Promoción: {venta['promocion']}")

def agregar_producto():
    fecha = input("Ingrese la fecha (dd-mm-aaaa): ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad de productos: "))
    precio = float(input("Ingrese el precio unitario del producto: "))
    promocion = input("¿Tiene promoción el producto?: Escriba True o False: ") == "True"
    nueva_venta = {"fecha": fecha, "producto": producto, "cantidad": cantidad, "precio": precio, "promocion": promocion}
    ventas.append(nueva_venta)
    print("El producto fue añadido correctamente.")

def calcular_suma_total():
    total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    print(f"La suma total de las ventas es: {total:.2f} soles")

def calcular_promedio():
    total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    promedio = total / len(ventas) if ventas else 0
    print(f"El promedio de ventas es: {promedio:.2f} soles")

def producto_mas_vendido():
    max_venta = max(ventas, key=lambda venta: venta['cantidad'])
    print(f"El producto con más unidades vendidas es: {max_venta['producto']} con {max_venta['cantidad']} unidades")

def mostrar_productos():
    productos = {venta['producto'] for venta in ventas}
    print("Listado de Productos:")
    for producto in productos:
        print(producto)

# MENÚ INTERACTIVO USANDO MATCH
while True:
    print("\nMenú de Opciones:")
    print("1. Mostrar el listado de ventas")
    print("2. Añadir un producto")
    print("3. Calcular la suma total de las ventas")
    print("4. Calcular el promedio de ventas")
    print("5. Mostrar el producto con más unidades vendidas")
    print("6. Mostrar el listado de productos")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            mostrar_ventas()
        case "2":
            agregar_producto()
        case "3":
            calcular_suma_total()
        case "4":
            calcular_promedio()
        case "5":
            producto_mas_vendido()
        case "6":
            mostrar_productos()
        case "7":
            print("Saliendo del programa.")
            print("\n")
            break
        case _:
            print("Opción inválida. Intente de nuevo.")
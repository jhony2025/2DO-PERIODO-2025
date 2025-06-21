# tienda_viveres.py

# Clase Producto representa un vívere de primera necesidad
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return cantidad * self.precio
        else:
            print(f"No hay suficiente stock de {self.nombre}.")
            return 0


# Clase Cliente representa a un comprador de la tienda
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_al_carrito(self, producto, cantidad):
        self.carrito.append((producto, cantidad))

    def pagar(self):
        total = 0
        for producto, cantidad in self.carrito:
            subtotal = producto.vender(cantidad)
            total += subtotal
        self.carrito.clear()
        return total


# Clase Tienda representa la tienda local de víveres
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def mostrar_productos(self):
        print(f"\nInventario de {self.nombre}:")
        for producto in self.inventario:
            print(f"{producto.nombre} - ${producto.precio} - Stock: {producto.stock}")


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear la tienda
    tienda = Tienda("Tienda El Ahorro")

    # Agregar productos de primera necesidad
    arroz = Producto("Arroz", 1.20, 100)
    leche = Producto("Leche", 0.90, 50)
    pan = Producto("Pan", 0.25, 200)
    queso = Producto("Queso", 3.50, 30)

    tienda.agregar_producto(arroz)
    tienda.agregar_producto(leche)
    tienda.agregar_producto(pan)
    tienda.agregar_producto(queso)

    tienda.mostrar_productos()

    # Cliente Doña Rosa realiza una compra
    cliente1 = Cliente("Doña Rosa")
    cliente1.agregar_al_carrito(arroz, 2)
    cliente1.agregar_al_carrito(pan, 10)
    total_pagado = cliente1.pagar()
    print(f"\n{cliente1.nombre} pagó: ${round(total_pagado, 2)}")

    # Cliente Johnny realiza una compra de aproximadamente $10
    cliente2 = Cliente("Johnny")
    cliente2.agregar_al_carrito(arroz, 2)     # 2 * 1.20 = 2.40
    cliente2.agregar_al_carrito(leche, 3)     # 3 * 0.90 = 2.70
    cliente2.agregar_al_carrito(queso, 1)     # 1 * 3.50 = 3.50
    cliente2.agregar_al_carrito(pan, 5)       # 5 * 0.25 = 1.25

    total_johnny = cliente2.pagar()
    print(f"\n{cliente2.nombre} pagó: ${round(total_johnny, 2)}")

    tienda.mostrar_productos()

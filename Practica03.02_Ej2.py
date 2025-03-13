class Producto:
    def __init__(self, codigo, nombre, precio):
        """Constructor de la clase Producto"""
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def calcular_total(self, unidades):
        return self.__precio * unidades

    def __str__(self):
        return f"{self.__nombre} - {self.__precio}€"


class Pedido:
    def __init__(self):
        """Constructor de la clase Pedido"""
        self.productos = []  
        self.cantidades = []  

    def agregar_producto(self, producto, cantidad):
        """Añade un producto con su cantidad al pedido"""
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return
        self.productos.append(producto)
        self.cantidades.append(cantidad)
        print(f"{cantidad} unidad(es) de {producto.get_nombre()} añadidas al pedido.")

    def total_pedido(self):
        """Calcula el precio total del pedido"""
        total = sum(prod.calcular_total(cant) for prod, cant in zip(self.productos, self.cantidades))
        return total

    def mostrar_productos(self):
        """Muestra los productos del pedido"""
        print("\nProductos en el pedido:")
        for prod, cant in zip(self.productos, self.cantidades):
            print(f"{prod.get_nombre()} - {cant} unidad(es) - Subtotal: {prod.calcular_total(cant)}€")
        print(f"Total del pedido: {self.total_pedido()}€\n")


if __name__ == "__main__":
    laptop = Producto(101, "Laptop", 750)
    mouse = Producto(102, "Mouse", 25)
    teclado = Producto(103, "Teclado", 50)

    mi_pedido = Pedido()
    mi_pedido.agregar_producto(laptop, 2)
    mi_pedido.agregar_producto(mouse, 3)
    mi_pedido.agregar_producto(teclado, 1)
    mi_pedido.mostrar_productos()

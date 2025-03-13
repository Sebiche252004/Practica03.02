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

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo.")

    def calcular_total(self, unidades):
        if unidades < 0:
            return "Las unidades no pueden ser negativas."
        return self.__precio * unidades

    def __str__(self):
        return f"Producto [Código: {self.__codigo}, Nombre: {self.__nombre}, Precio: {self.__precio}€]"


if __name__ == "__main__":
    producto1 = Producto(101, "Laptop", 750)
    
    print(producto1)  

    unidades = 3
    total = producto1.calcular_total(unidades)
    print(f"Total por {unidades} unidades: {total}€")

    producto1.set_precio(800)
    print(f"Nuevo precio: {producto1.get_precio()}€")

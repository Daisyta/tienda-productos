class Producto:
    def __init__(self,nombre,precio,categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    def update_price(self, percent_change, is_increased):
#update_price(self, percent_change, is_increased) : actualiza el precio del producto. Si is_increased es True, el precio debería aumentar en el porcentaje de cambio proporcionado. Si es False, el precio debe disminuir en el cambio porcentual proporcionado.
        if is_increased == True:
            self.price = self.price + (self.price * percent_change)
        elif is_increased == False:
            self.price = self.price - (self.price * percent_change)
        return self
    def print_info(self):
#print_info (self) : imprime el nombre del producto, su categoría y su precio.     
        print(f"Producto: {self.nombre}, Precio {self.precio}, Categoria {self.categoria}")
        return self
    def inflationo(self, percent_increase):
        self.price = self.price+(self.price * percent_increase)
        return self
    def set_clearance (self, categoria, percent_discount):
        for x in self.listaproductos:
            if categoria == x.categoria:
                x.price = x.price - (x.price * percent_discount)
            print(x.price)
        return self

class Tienda:
    def __init__(self,nombre):
        self.nombre = nombre
        self.listaproductos = []
    def add_product (self, new_product):
        self.listaproductos.append(new_product)
        return self #append se ocupa para aggregar
    def sell_product(self,id): 
        self.listaproductos.pop(id) #pop se ocupa para eliminar algo de acuerdo al id
    def mostrar_productos (self):
        for product in self.listaproductos:
            product.print_info()
        return self

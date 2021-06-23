from  clases.tienda import Tienda
from  clases.producto import Producto

tienda1= Tienda("Brunito")
huevos= Producto("huevos", 300, "comida")
cloro= Producto("cloro",800,"limpieza")
manzanas= Producto("manzanas",900,"frutas")


tienda1.add_product(huevos)
tienda1.add_product(cloro)
tienda1.add_product(manzanas)
#huevos.print_info()
#print tienda1.listaproductos()
#print (tienda1.mostrar_productos
tienda1.mostrar_productos()


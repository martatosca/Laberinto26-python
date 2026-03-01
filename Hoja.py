from ElementoMapa import ElementoMapa
#Hoja representa elementos que no tienen hijos
class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()
    #metodos para gestionar los hijos 
    def agregar_hijo(self, hijo):
        raise TypeError(f"{self.__class__.__name__} es una hoja y no acepta hijos")

    def eliminar_hijo(self, hijo):
        raise TypeError(f"{self.__class__.__name__} es una hoja y no acepta hijos")

    def obtener_hijos(self):
        return [] #las hojas no tienen hijos
    
    def recorrer(self):
        yield self


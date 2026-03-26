from ElementoMapa import ElementoMapa
class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()
    def agregar_hijo(self, hijo):
        raise TypeError(f"{self.__class__.__name__} es una hoja y no acepta hijos")

    def eliminar_hijo(self, hijo):
        raise TypeError(f"{self.__class__.__name__} es una hoja y no acepta hijos")

    def obtener_hijos(self):
        return []
    
    def recorrer(self):
        yield self

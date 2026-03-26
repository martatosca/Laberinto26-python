from ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):
    

    def __init__(self, forma=None):
        super().__init__()
        self.hijos = []
        self._forma = forma
    
    @property
    def forma(self):
        
        return self._forma
    
    @forma.setter
    def forma(self, value):
        
        self._forma = value
    
    def obtener_orientaciones(self):
        
        if self._forma:
            return self._forma.obtener_orientaciones()
        return []  

    def agregar_hijo(self, hijo):
        if hijo is None:
            raise ValueError("No se puede agregar un hijo None")
        hijo.padre = self
        self.hijos.append(hijo)

    def eliminar_hijo(self, hijo):
        if hijo not in self.hijos:
            raise ValueError("Ese hijo no está en la lista de hijos")
        self.hijos.remove(hijo)
        hijo.padre = None

    def obtener_hijos(self):
        return list(self.hijos)

    def recorrer(self):
        'Iterador interno primero recorre el propio contenedor y luego recorre recursivamente sus hijos'
        yield self
        for h in self.hijos:
            yield from h.recorrer()

    def entrar(self):
        print(f"Entrando en {self.__class__.__name__}")

    def __str__(self):
        return f"{self.__class__.__name__} con {len(self.hijos)} hijos"

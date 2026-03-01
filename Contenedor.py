from ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):
    """
    Composite del patrón Composite: Mantiene una lista de hijos ElementoMapa y permite recorrerlos (Iterator).
    """

    def __init__(self):
        super().__init__()
        self.hijos = []  

    def agregar_hijo(self, hijo):
        if hijo is None:
            raise ValueError("No se puede agregar un hijo None")
        hijo.padre = self
        self.hijos.append(hijo)

    def eliminar_hijo(self, hijo):
        # Si no está, avisamos con un error
        if hijo not in self.hijos:
            raise ValueError("Ese hijo no está en la lista de hijos")
        self.hijos.remove(hijo)
        hijo.padre = None

    def obtener_hijos(self):
        # Devolvemos copia para que no modifiquen la lista desde fuera
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
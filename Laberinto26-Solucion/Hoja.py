# Hoja es la interfaz de los elementos simples del laberinto (Leaf en Composite)
from ElementoMapa import ElementoMapa


class Hoja(ElementoMapa):
    """Representa los elementos simples del laberinto (pared, puerta, bomba…)."""

    def recorrer(self, bloque):
        """Visita este elemento con el bloque y no tiene hijos que recorrer."""
        print(str(self))
        bloque(self)

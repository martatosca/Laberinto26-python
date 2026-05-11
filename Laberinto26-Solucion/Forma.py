# Forma es la implementación del patrón Bridge para los contenedores.
# Almacena las orientaciones (singletons) y los elementos de mapa por dirección.
import random


class Forma:
    """Implementación del puente (Bridge) que almacena las orientaciones
    y los elementos del mapa asociados a cada dirección."""

    def __init__(self):
        self.orientaciones = []   # lista de objetos Orientacion (singletons)
        self.num = 0

    def agregar_orientacion(self, orientacion):
        """Añade una orientación a la lista."""
        self.orientaciones.append(orientacion)

    def eliminar_orientacion(self, orientacion):
        """Elimina una orientación de la lista."""
        if orientacion in self.orientaciones:
            self.orientaciones.remove(orientacion)

    def obtener_elemento(self, una_or):
        """Obtiene el ElementoMapa en una dirección (Bridge: delega en la orientación)."""
        return una_or.obtener_elemento(self)

    def obtener_orientacion_aleatoria(self):
        """Devuelve una orientación aleatoria de la lista."""
        if self.orientaciones:
            idx = random.randint(0, len(self.orientaciones) - 1)
            return self.orientaciones[idx]
        return None

    def poner_en(self, una_or, un_em):
        """Coloca un ElementoMapa en una dirección (Bridge: delega en la orientación)."""
        una_or.poner_elemento(un_em, self)

    def __str__(self):
        return self.__class__.__name__

# Modo: define la interfaz de los comportamientos de los bichos (Strategy)
from abc import ABC, abstractmethod


class Modo(ABC):
    """Interfaz del patron Strategy para los modos de comportamiento de los bichos."""

    def actua(self, bicho):
        """Secuencia completa de acciones: caminar, atacar, dormir."""
        self.camina(bicho)
        self.ataca(bicho)
        self.duerme(bicho)

    def ataca(self, bicho):
        """El bicho ejecuta su ataque."""
        bicho.atacar()

    def camina(self, bicho):
        """El bicho se mueve en una direccion aleatoria."""
        or_ = bicho.obtener_orientacion_aleatoria()
        or_.caminar(bicho)

    @abstractmethod
    def duerme(self, bicho):
        """Comportamiento de descanso (cada subclase define la duracion)."""
        pass

    def es_agresivo(self):
        return False

    def es_perezoso(self):
        return False

    def __str__(self):
        return self.__class__.__name__

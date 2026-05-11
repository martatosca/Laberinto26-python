# Orientacion define la interfaz de las orientaciones de los contenedores
from abc import ABC, abstractmethod


class Orientacion(ABC):
    """Interfaz del patron Bridge para las orientaciones.
    Cada subclase sabe como acceder/modificar el slot correspondiente en una Forma."""

    @abstractmethod
    def aceptar(self, visitor, forma):
        pass

    @abstractmethod
    def caminar(self, bicho):
        pass

    @abstractmethod
    def obtener_elemento(self, forma):
        pass

    @abstractmethod
    def poner_elemento(self, em, forma):
        pass

    @abstractmethod
    def recorrer(self, bloque, forma):
        pass

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__


from LaberintoFactory import LaberintoFactory
from ParedFuego import ParedFuego
from PuertaFuego import PuertaFuego

class LaberintoFuegoFactory(LaberintoFactory):
    """
    ConcreteFactory del patrón Abstract Factory.
    Crea una familia de productos con temática de FUEGO:
    - ParedFuego
    - PuertaFuego
    """
    
    def fabricarPared(self):
        """Crea una ParedFuego"""
        return ParedFuego()
    
    def fabricarPuerta(self, lado1=None, lado2=None):
        """Crea una PuertaFuego"""
        return PuertaFuego(lado1, lado2)
    
    def __str__(self):
        return "LaberintoFuegoFactory"

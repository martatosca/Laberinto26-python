from LaberintoFactory import LaberintoFactory
from ParedBomba import ParedBomba
from PuertaBomba import PuertaBomba

class LaberintoBombasFactory(LaberintoFactory):
    """
    ConcreteFactory del patrón Abstract Factory.
    Crea una familia de productos con temática de BOMBAS:
    - ParedBomba
    - PuertaBomba
    """
    
    def fabricarPared(self):
        """Crea una ParedBomba"""
        return ParedBomba()
    
    def fabricarPuerta(self, lado1=None, lado2=None):
        """Crea una PuertaBomba"""
        return PuertaBomba(lado1, lado2)
    
    def __str__(self):
        return "LaberintoBombasFactory"

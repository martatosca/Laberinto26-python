from abc import ABC, abstractmethod

class LaberintoFactory(ABC):
    """
    AbstractFactory del patrón Abstract Factory.
    Define la interfaz para crear familias de productos relacionados:
    - Pared (y sus variantes)
    - Puerta (y sus variantes)
    """
    
    @abstractmethod
    def fabricarPared(self):
        """Crea una Pared del tipo correspondiente a esta factory"""
        pass
    
    @abstractmethod
    def fabricarPuerta(self, lado1=None, lado2=None):
        """Crea una Puerta del tipo correspondiente a esta factory"""
        pass

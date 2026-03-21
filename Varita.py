from abc import ABC, abstractmethod

class Varita(ABC):
    """
    TARGET del patrón Adapter.
    
    Define la interfaz que utiliza el Client (Personaje).
    El Personaje usa la Varita para cambiar el modo de algo.
    """
    
    @abstractmethod
    def cambiar_modo(self):
        """Cambia el modo del objetivo"""
        pass

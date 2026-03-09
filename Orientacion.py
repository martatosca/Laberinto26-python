from abc import ABC, abstractmethod

class Orientacion(ABC):
    """
    Strategy abstracto para las orientaciones de una habitación.
    Define la interfaz común para todas las orientaciones.
    """
    
    @abstractmethod
    def obtener_nombre(self) -> str:
        """Devuelve el nombre de la orientación"""
        pass
    
    @abstractmethod
    def obtener_opuesta(self) -> "Orientacion":
        """Devuelve la orientación opuesta"""
        pass
    
    def __str__(self):
        return self.obtener_nombre()

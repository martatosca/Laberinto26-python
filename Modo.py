from abc import ABC, abstractmethod

class Modo(ABC):
    """
    Strategy abstracto para los modos de comportamiento de un Bicho.
    Define la interfaz común para todos los modos.
    """
    
    @abstractmethod
    def actuar(self, bicho) -> str:
        """Define cómo actúa el bicho según este modo"""
        pass
    
    @abstractmethod
    def caminar(self, bicho) -> str:
        """Define cómo camina el bicho según este modo"""
        pass
    
    @abstractmethod
    def atacar(self, bicho) -> str:
        """Define cómo ataca el bicho según este modo"""
        pass
    
    @abstractmethod
    def dormir(self, bicho) -> str:
        """Define cómo duerme el bicho según este modo"""
        pass
    
    @abstractmethod
    def obtener_nombre(self) -> str:
        """Devuelve el nombre del modo"""
        pass
    
    def __str__(self):
        return self.obtener_nombre()

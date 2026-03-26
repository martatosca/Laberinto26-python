from abc import ABC, abstractmethod
from typing import List

class Forma(ABC):
    
    
    @abstractmethod
    def obtener_orientaciones(self) -> List:
        
        pass
    
    @abstractmethod
    def obtener_nombre(self) -> str:
        
        pass
    
    @abstractmethod
    def num_orientaciones(self) -> int:
        
        pass
    
    def __str__(self):
        return self.obtener_nombre()

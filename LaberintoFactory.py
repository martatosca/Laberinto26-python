from abc import ABC, abstractmethod

class LaberintoFactory(ABC):
    
    
    @abstractmethod
    def fabricarPared(self):
        
        pass
    
    @abstractmethod
    def fabricarPuerta(self, lado1=None, lado2=None):
        
        pass

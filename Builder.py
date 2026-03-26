from abc import ABC, abstractmethod

class Builder(ABC):
    
    
    @abstractmethod
    def fabricarLaberinto(self):
        
        pass
    
    @abstractmethod
    def fabricarHabitacion(self, num: int):
        
        pass
    
    @abstractmethod
    def fabricarPuerta(self, lado1, lado2):
        
        pass
    
    @abstractmethod
    def fabricarPared(self):
        
        pass
    
    @abstractmethod
    def fabricarBombaEn(self, contenedor):
        
        pass
    
    @abstractmethod
    def fabricarArmario(self, num: int, contenedor):
        
        pass
    
    @abstractmethod
    def fabricarBichoModo(self, str_modo: str, posicion: int):
        
        pass
    
    @abstractmethod
    def obtenerLaberinto(self):
        
        pass

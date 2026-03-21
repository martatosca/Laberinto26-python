from abc import ABC, abstractmethod

class Builder(ABC):
    """
    Builder: Interfaz abstracta que define los métodos para crear partes del Laberinto.
    Especifica una interface abstracta para crear partes de un Producto.
    """
    
    @abstractmethod
    def fabricarLaberinto(self):
        """Crea el laberinto vacío"""
        pass
    
    @abstractmethod
    def fabricarHabitacion(self, num: int):
        """Crea una habitación con el número dado"""
        pass
    
    @abstractmethod
    def fabricarPuerta(self, lado1, lado2):
        """Crea una puerta entre dos lados"""
        pass
    
    @abstractmethod
    def fabricarPared(self):
        """Crea una pared"""
        pass
    
    @abstractmethod
    def fabricarBombaEn(self, contenedor):
        """Crea una bomba en el contenedor dado"""
        pass
    
    @abstractmethod
    def fabricarArmario(self, num: int, contenedor):
        """Crea un armario dentro de un contenedor"""
        pass
    
    @abstractmethod
    def fabricarBichoModo(self, str_modo: str, posicion: int):
        """Crea un bicho con el modo y posición indicados"""
        pass
    
    @abstractmethod
    def obtenerLaberinto(self):
        """Devuelve el laberinto construido (GetResult)"""
        pass

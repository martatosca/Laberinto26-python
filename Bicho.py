from Modo import Modo
from Agresivo import Agresivo

class Bicho:
    """
    Context del patrón Strategy para Modo.
    Representa una criatura del laberinto con un modo de comportamiento intercambiable.
    """
    
    def __init__(self, nombre: str, modo: Modo = None):
        self.nombre = nombre
        self._modo = modo if modo else Agresivo()  # Modo por defecto: Agresivo
        self.posicion = None  # Habitación donde se encuentra
    
    @property
    def modo(self) -> Modo:
        return self._modo
    
    @modo.setter
    def modo(self, nuevo_modo: Modo):
        """Permite cambiar el modo en tiempo de ejecución (Strategy intercambiable)"""
        print(f"{self.nombre} cambia de modo {self._modo} a {nuevo_modo}")
        self._modo = nuevo_modo
    
    def actuar(self):
        """Delega la acción al Strategy actual"""
        return self._modo.actuar(self)
    
    def entrar_habitacion(self, habitacion):
        """El bicho entra en una habitación"""
        self.posicion = habitacion
        print(f"{self.nombre} ha entrado en la habitación {habitacion.id}")
    
    def __str__(self):
        return f"Bicho({self.nombre}, modo={self._modo})"

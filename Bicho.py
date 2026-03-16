from Modo import Modo
from Agresivo import Agresivo

class Bicho:
    """
    Context del patrón Strategy para Modo.
    Representa una criatura del laberinto con un modo de comportamiento intercambiable.
    """
    
    def __init__(self, nombre: str, modo: Modo = None, vidas: int = 3, poder: int = 10):
        self.nombre = nombre
        self._modo = modo if modo else Agresivo()  # Modo por defecto: Agresivo
        self.posicion = None  # Habitación donde se encuentra
        self.vidas = vidas
        self.poder = poder
    
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
    
    def caminar(self):
        """Delega el caminar al Strategy actual"""
        return self._modo.caminar(self)
    
    def atacar(self):
        """Delega el atacar al Strategy actual"""
        return self._modo.atacar(self)
    
    def dormir(self):
        """Delega el dormir al Strategy actual"""
        return self._modo.dormir(self)
    
    def entrar_habitacion(self, habitacion):
        """El bicho entra en una habitación"""
        self.posicion = habitacion
        print(f"{self.nombre} ha entrado en la habitación {habitacion.id}")
    
    def recibir_dano(self, cantidad: int):
        """El bicho recibe daño y pierde vidas"""
        self.vidas -= cantidad
        print(f"{self.nombre} recibe {cantidad} de daño. Vidas restantes: {self.vidas}")
        if self.vidas <= 0:
            print(f"{self.nombre} ha sido derrotado!")
    
    def esta_vivo(self) -> bool:
        return self.vidas > 0
    
    def __str__(self):
        return f"Bicho({self.nombre}, modo={self._modo}, vidas={self.vidas}, poder={self.poder})"

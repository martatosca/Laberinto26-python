from Ente import Ente
from Varita import Varita

class Personaje(Ente):
    """
    CLIENT del patrón Adapter.
    
    El Personaje es el cliente que usa la Varita (Target) para interactuar
    con los Bichos. Usa BichoAdapter para cambiar el modo de los bichos.
    
    También hereda de Ente según el diagrama de clases original.
    """
    
    def __init__(self, nombre: str, vidas: int = 5, poder: int = 10):
        super().__init__(vidas, poder)
        self.nombre = nombre
        self._varita = None  # Referencia a la Varita (Target)
    
    @property
    def varita(self) -> Varita:
        return self._varita
    
    @varita.setter
    def varita(self, value: Varita):
        self._varita = value
    
    def usar_varita(self):
        """
        El cliente usa la Varita (Target) para cambiar el modo.
        La Varita puede ser un BichoAdapter que adapta un Bicho.
        """
        if self._varita is None:
            print(f"{self.nombre} no tiene varita!")
            return None
        
        print(f"{self.nombre} usa la varita mágica...")
        return self._varita.cambiar_modo()
    
    def cambiar_modo_bicho(self, varita: Varita):
        """
        Método alternativo: recibe la varita como parámetro.
        Útil cuando el personaje quiere usar una varita específica.
        """
        print(f"{self.nombre} apunta con la varita...")
        return varita.cambiar_modo()
    
    def entrar_habitacion(self, habitacion):
        """El personaje entra en una habitación"""
        self.posicion = habitacion
        print(f"{self.nombre} ha entrado en la habitación {habitacion.id}")
    
    def __str__(self):
        return f"Personaje({self.nombre}, vidas={self.vidas})"

from Ente import Ente
from Varita import Varita

class Personaje(Ente):
    
    
    def __init__(self, nombre: str, vidas: int = 5, poder: int = 10):
        super().__init__(vidas, poder)
        self.nombre = nombre
        self._varita = None
    
    @property
    def varita(self) -> Varita:
        return self._varita
    
    @varita.setter
    def varita(self, value: Varita):
        self._varita = value
    
    def usar_varita(self):
        
        if self._varita is None:
            print(f"{self.nombre} no tiene varita!")
            return None
        
        print(f"{self.nombre} usa la varita mágica...")
        return self._varita.cambiar_modo()
    
    def cambiar_modo_bicho(self, varita: Varita):
        
        print(f"{self.nombre} apunta con la varita...")
        return varita.cambiar_modo()
    
    def entrar_habitacion(self, habitacion):
        
        self.posicion = habitacion
        print(f"{self.nombre} ha entrado en la habitación {habitacion.id}")
    
    def __str__(self):
        return f"Personaje({self.nombre}, vidas={self.vidas})"

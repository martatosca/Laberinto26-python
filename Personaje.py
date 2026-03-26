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
    
    def atacarA(self, objetivo):
        self.notificar("atacar", objetivo)
    
    def entrar_habitacion(self, habitacion):
        
        self.posicion = habitacion
        print(f"{self.nombre} ha entrado en la habitación {habitacion.id}")
        self.notificar("entrar_habitacion", habitacion)
    
    def recibir_dano(self, cantidad: int):
        super().recibir_dano(cantidad)
        print(f"{self.nombre} recibe {cantidad} de daño. Vidas restantes: {self.vidas}")
        if not self.esta_vivo():
            print(f"{self.nombre} ha sido derrotado!")
            self.notificar("derrotado", None)
    
    def __str__(self):
        return f"Personaje({self.nombre}, vidas={self.vidas})"

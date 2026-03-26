from Modo import Modo
from Agresivo import Agresivo
from Ente import Ente

class Bicho(Ente):
    
    
    def __init__(self, nombre: str, modo: Modo = None, vidas: int = 3, poder: int = 10):
        super().__init__(vidas, poder)
        self.nombre = nombre
        self._modo = modo if modo else Agresivo()
    
    @property
    def modo(self) -> Modo:
        return self._modo
    
    @modo.setter
    def modo(self, nuevo_modo: Modo):
        
        print(f"{self.nombre} cambia de modo {self._modo} a {nuevo_modo}")
        self._modo = nuevo_modo
    
    def actua(self):
        
        return self._modo.actua(self)
    
    def caminar(self):
        
        return self._modo.caminar(self)
    
    def camina(self):
        
        return self._modo.camina(self)
    
    def atacar(self):
        
        return self._modo.atacar(self)
    
    def duerme(self):
        
        return self._modo.duerme(self)
    
    def entrar_habitacion(self, habitacion):
        
        self.posicion = habitacion
        print(f"{self.nombre} ha entrado en la habitación {habitacion.id}")
    
    def recibir_dano(self, cantidad: int):
        
        super().recibir_dano(cantidad)
        print(f"{self.nombre} recibe {cantidad} de daño. Vidas restantes: {self.vidas}")
        if not self.esta_vivo():
            print(f"{self.nombre} ha sido derrotado!")
    
    def __str__(self):
        return f"Bicho({self.nombre}, modo={self._modo}, vidas={self.vidas}, poder={self.poder})"

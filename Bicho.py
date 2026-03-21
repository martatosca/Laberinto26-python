from Modo import Modo
from Agresivo import Agresivo
from Ente import Ente

class Bicho(Ente):
    """
    Context del patrón Strategy/Template Method para Modo.
    Representa una criatura del laberinto con un modo de comportamiento intercambiable.
    Hereda de Ente (vidas, poder, posicion, esta_vivo).
    """
    
    def __init__(self, nombre: str, modo: Modo = None, vidas: int = 3, poder: int = 10):
        super().__init__(vidas, poder)  # Llama al constructor de Ente
        self.nombre = nombre
        self._modo = modo if modo else Agresivo()  # Modo por defecto: Agresivo
    
    @property
    def modo(self) -> Modo:
        return self._modo
    
    @modo.setter
    def modo(self, nuevo_modo: Modo):
        """Permite cambiar el modo en tiempo de ejecución (Strategy intercambiable)"""
        print(f"{self.nombre} cambia de modo {self._modo} a {nuevo_modo}")
        self._modo = nuevo_modo
    
    def actua(self):
        """Delega al TEMPLATE METHOD del modo - ejecuta la secuencia completa"""
        return self._modo.actua(self)
    
    def caminar(self):
        """Delega el caminar al modo actual (estilo de caminar)"""
        return self._modo.caminar(self)
    
    def camina(self):
        """
        Delega al modo para que el bicho camine usando orientación aleatoria.
        Según código del profesor: obtiene orientación aleatoria y camina.
        """
        return self._modo.camina(self)
    
    def atacar(self):
        """Delega el atacar al modo actual"""
        return self._modo.atacar(self)
    
    def duerme(self):
        """Delega el duerme al modo actual"""
        return self._modo.duerme(self)
    
    def entrar_habitacion(self, habitacion):
        """El bicho entra en una habitación"""
        self.posicion = habitacion
        print(f"{self.nombre} ha entrado en la habitación {habitacion.id}")
    
    def recibir_dano(self, cantidad: int):
        """Sobreescribe para mensajes específicos del bicho"""
        super().recibir_dano(cantidad)
        print(f"{self.nombre} recibe {cantidad} de daño. Vidas restantes: {self.vidas}")
        if not self.esta_vivo():
            print(f"{self.nombre} ha sido derrotado!")
    
    def __str__(self):
        return f"Bicho({self.nombre}, modo={self._modo}, vidas={self.vidas}, poder={self.poder})"

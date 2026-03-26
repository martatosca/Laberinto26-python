class Ente:
    
    
    def __init__(self, vidas: int = 3, poder: int = 10):
        self.vidas = vidas
        self.poder = poder
        self.posicion = None
        self._juego = None
    
    @property
    def juego(self):
        return self._juego
    
    @juego.setter
    def juego(self, value):
        self._juego = value
    
    def notificar(self, evento: str, datos=None):
        if self._juego:
            self._juego.notificar(self, evento, datos)
    
    def esta_vivo(self) -> bool:
        
        return self.vidas > 0
    
    def recibir_dano(self, cantidad: int):
        
        self.vidas -= cantidad
        if self.vidas <= 0:
            self.vidas = 0
    
    def __str__(self):
        return f"Ente(vidas={self.vidas}, poder={self.poder})"

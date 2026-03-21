class Ente:
    """
    Clase base para entidades con vida y poder.
    Es la clase padre de Personaje y podría ser de Bicho también.
    """
    
    def __init__(self, vidas: int = 3, poder: int = 10):
        self.vidas = vidas
        self.poder = poder
        self.posicion = None  # Habitación donde se encuentra
    
    def esta_vivo(self) -> bool:
        """Un ente está vivo si tiene vidas > 0"""
        return self.vidas > 0
    
    def recibir_dano(self, cantidad: int):
        """El ente recibe daño y pierde vidas"""
        self.vidas -= cantidad
        if self.vidas <= 0:
            self.vidas = 0
    
    def __str__(self):
        return f"Ente(vidas={self.vidas}, poder={self.poder})"

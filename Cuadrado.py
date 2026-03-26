from Forma import Forma
from Orientaciones import Norte, Sur, Este, Oeste
from typing import List

class Cuadrado(Forma):
    
    
    def __init__(self):
        self.norte = Norte()
        self.sur = Sur()
        self.este = Este()
        self.oeste = Oeste()
    
    def obtener_orientaciones(self) -> List:
        
        return [self.norte, self.sur, self.este, self.oeste]
    
    def obtener_nombre(self) -> str:
        return "Cuadrado"
    
    def num_orientaciones(self) -> int:
        return 4
    
    def __str__(self):
        return "Cuadrado(N, S, E, O)"

from Forma import Forma
from Orientaciones import Noreste, Noroeste, Sureste, Suroeste
from typing import List

class Rombo(Forma):
    
    
    def __init__(self):
        self.noreste = Noreste()
        self.noroeste = Noroeste()
        self.sureste = Sureste()
        self.suroeste = Suroeste()
    
    def obtener_orientaciones(self) -> List:
        
        return [self.noreste, self.noroeste, self.sureste, self.suroeste]
    
    def obtener_nombre(self) -> str:
        return "Rombo"
    
    def num_orientaciones(self) -> int:
        return 4
    
    def __str__(self):
        return "Rombo(NE, NO, SE, SO)"

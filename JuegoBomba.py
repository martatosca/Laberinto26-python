from Juego import Juego
from ParedBomba import ParedBomba

class JuegoBomba(Juego):
    def __init__(self):
        super().__init__()
    
    def fabricarPared(self):
        return ParedBomba()
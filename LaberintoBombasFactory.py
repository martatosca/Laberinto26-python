from LaberintoFactory import LaberintoFactory
from ParedBomba import ParedBomba
from PuertaBomba import PuertaBomba

class LaberintoBombasFactory(LaberintoFactory):
    
    
    def fabricarPared(self):
        
        return ParedBomba()
    
    def fabricarPuerta(self, lado1=None, lado2=None):
        
        return PuertaBomba(lado1, lado2)
    
    def __str__(self):
        return "LaberintoBombasFactory"

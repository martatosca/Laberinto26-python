from LaberintoFactory import LaberintoFactory
from ParedFuego import ParedFuego
from PuertaFuego import PuertaFuego

class LaberintoFuegoFactory(LaberintoFactory):
    
    
    def fabricarPared(self):
        
        return ParedFuego()
    
    def fabricarPuerta(self, lado1=None, lado2=None):
        
        return PuertaFuego(lado1, lado2)
    
    def __str__(self):
        return "LaberintoFuegoFactory"

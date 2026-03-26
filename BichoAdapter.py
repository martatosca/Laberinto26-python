from Varita import Varita

class BichoAdapter(Varita):
    
    
    def __init__(self, bicho):
        
        self._bicho = bicho
    
    @property
    def bicho(self):
        return self._bicho
    
    @bicho.setter
    def bicho(self, value):
        self._bicho = value
    
    def cambiar_modo(self):
        
        if self._bicho and self._bicho.modo:
            nuevo_modo = self._bicho.modo.cambiar_modo(self._bicho)
            return nuevo_modo
        return None
    
    def __str__(self):
        return f"BichoAdapter({self._bicho})"

from ElementoMapa import ElementoMapa

class Habitacion (ElementoMapa):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
    @property
    def norte(self):
        return self._norte
    @property
    def sur(self):
        return self._sur
    @property
    def este(self):
        return self._este
    @property
    def oeste(self):
        return self._oeste
    
       
        
    
        
        
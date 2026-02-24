from Pared import Pared
class ParedBomba (Pared):
    
    def __init__(self):
        super().__init__()
        self.activa=False
        
    @property
    def activa(self):
        return self._activa
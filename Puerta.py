from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.abierta=False
        self.lado1=None
        self.lado2=None
    
    @property
    def abierta(self):
        return self._abierta
    @property
    def lado1(self):
        return self._lado1
    @property
    def lado2(self):
        return self._lado2
    
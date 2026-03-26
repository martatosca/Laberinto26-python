from Decorator import Decorator
from ElementoMapa import ElementoMapa

class Bomba(Decorator):
    
    
    def __init__(self, componente: ElementoMapa, activa: bool = True):
        super().__init__(componente)
        self.activa = activa
    
    def entrar(self):
        
        if self.activa:
            print("💥 BOOM! La bomba explota.")
            self.activa = False
        else:
            print("La bomba ya ha explotado.")
        super().entrar()
    
    def __str__(self):
        estado = "activa" if self.activa else "explotada"
        return f"Bomba[{estado}]({self._componente})"

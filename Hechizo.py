from Decorator import Decorator
from ElementoMapa import ElementoMapa

class Hechizo(Decorator):
    
    
    def __init__(self, componente: ElementoMapa, tipo_hechizo: str = "misterioso"):
        super().__init__(componente)
        self.tipo_hechizo = tipo_hechizo
        self.activo = True
    
    def entrar(self):
        
        if self.activo:
            print(f"✨ Un hechizo {self.tipo_hechizo} te afecta...")
        super().entrar()
    
    def desactivar(self):
        
        self.activo = False
        print(f"El hechizo {self.tipo_hechizo} ha sido desactivado.")
    
    def __str__(self):
        estado = "activo" if self.activo else "inactivo"
        return f"Hechizo[{self.tipo_hechizo},{estado}]({self._componente})"

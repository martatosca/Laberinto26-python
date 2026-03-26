from ElementoMapa import ElementoMapa
from typing import Iterator

class Decorator(ElementoMapa):
    
    
    def __init__(self, componente: ElementoMapa):
        super().__init__()
        self._componente = componente
    
    @property
    def componente(self):
        return self._componente
    
    def entrar(self):
        
        self._componente.entrar()
    
    def recorrer(self) -> Iterator[ElementoMapa]:
        
        yield self
        yield from self._componente.recorrer()
    
    def __str__(self):
        return f"Decorator({self._componente})"

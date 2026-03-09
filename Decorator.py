from ElementoMapa import ElementoMapa
from typing import Iterator

class Decorator(ElementoMapa):
    """
    Decorator base del patrón Decorator.
    Envuelve un ElementoMapa y delega las operaciones a él.
    """
    
    def __init__(self, componente: ElementoMapa):
        super().__init__()
        self._componente = componente
    
    @property
    def componente(self):
        return self._componente
    
    def entrar(self):
        """Delega al componente envuelto"""
        self._componente.entrar()
    
    def recorrer(self) -> Iterator[ElementoMapa]:
        """Recorre el decorador y luego el componente"""
        yield self
        yield from self._componente.recorrer()
    
    def __str__(self):
        return f"Decorator({self._componente})"

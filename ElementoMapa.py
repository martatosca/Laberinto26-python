from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    @abstractmethod
    def entrar(self):
        pass

# Abrir: comando para abrir una puerta del laberinto
from Comando import Comando


class Abrir(Comando):
    """Comando concreto que abre el receptor (una Puerta)."""

    def ejecutar(self, alguien):
        self.receptor.abrir()

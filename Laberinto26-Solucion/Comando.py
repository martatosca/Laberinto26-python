# Comando: interfaz de los comandos del laberinto (patron Command)
from abc import ABC, abstractmethod


class Comando(ABC):
    """Interfaz del patron Command para acciones sobre elementos del mapa."""

    def __init__(self):
        self.receptor = None

    @abstractmethod
    def ejecutar(self, alguien):
        """Ejecuta el comando sobre su receptor."""
        pass

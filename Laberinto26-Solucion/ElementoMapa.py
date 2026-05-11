# ElementoMapa es la interfaz común de los elementos del laberinto
from abc import ABC, abstractmethod


class ElementoMapa(ABC):
    """Interfaz base del patrón Composite para los elementos del laberinto."""

    def __init__(self):
        self.comandos = []  # lista de Comandos asociados (patrón Command)

    # --- Comandos ---
    def agregar_comando(self, comando):
        """Asocia un comando a este elemento."""
        self.comandos.append(comando)

    def eliminar_comando(self, comando):
        """Elimina un comando asociado."""
        if comando in self.comandos:
            self.comandos.remove(comando)

    # --- Visitor ---
    @abstractmethod
    def aceptar(self, visitor):
        """Acepta un visitante (patrón Visitor)."""
        pass

    # --- Comportamiento ---
    @abstractmethod
    def entrar(self, alguien):
        """Define qué ocurre cuando alguien entra en este elemento."""
        pass

    @abstractmethod
    def recorrer(self, bloque):
        """Recorre este elemento aplicando el bloque (callable) a cada subelemento."""
        pass

    # --- Consultas tipo ---
    def es_puerta(self):
        return False

    def es_bomba(self):
        return False

    def es_tunel(self):
        return False

    def es_armario(self):
        return False

    def __str__(self):
        return self.__class__.__name__

# ElementoMapa es la interfaz común de los elementos del laberinto
# Actualizado con las consultas de tipo de las extensiones basicas
from abc import ABC, abstractmethod


class ElementoMapa(ABC):
    """Interfaz base del patrón Composite para los elementos del laberinto."""

    def __init__(self):
        self.comandos = []

    def agregar_comando(self, comando):
        self.comandos.append(comando)

    def eliminar_comando(self, comando):
        if comando in self.comandos:
            self.comandos.remove(comando)

    @abstractmethod
    def aceptar(self, visitor):
        pass

    @abstractmethod
    def entrar(self, alguien):
        pass

    @abstractmethod
    def recorrer(self, bloque):
        pass

    # --- Consultas tipo (originales) ---
    def es_puerta(self):            return False
    def es_bomba(self):             return False
    def es_tunel(self):             return False
    def es_armario(self):           return False

    # --- Consultas tipo (extensiones basicas) ---
    def es_trampa(self):            return False
    def es_escalera(self):          return False
    def es_pared_transparente(self): return False

    def __str__(self):
        return self.__class__.__name__

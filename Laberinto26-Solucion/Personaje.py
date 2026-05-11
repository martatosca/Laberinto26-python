# Personaje: el protagonista del juego
from Ente import Ente


class Personaje(Ente):
    """Personaje es el protagonista del juego del laberinto."""

    def __init__(self):
        super().__init__()
        self.nombre = ""

    def buscar_enemigo(self):
        """Pide al juego un bicho en su misma posicion."""
        return self.juego.buscar_bicho()

    def ir_a(self, orientacion):
        """Mueve al personaje en la direccion indicada."""
        orientacion.caminar(self)

    def ir_al_norte(self):
        from Orientaciones import Norte
        Norte().caminar(self)

    def muero(self):
        self.juego.muere_personaje()

    def __str__(self):
        return self.nombre

# Tunel: Hoja que puede conectar con otro laberinto (Proxy virtual)
from Hoja import Hoja


class Tunel(Hoja):
    """Tunel es una Hoja que actua como Proxy Virtual: su laberinto
    se crea (clona) en el primer acceso."""

    def __init__(self):
        super().__init__()
        self.laberinto = None  # se crea al primer acceso (Proxy Virtual)

    # --- Visitor ---
    def aceptar(self, visitor):
        visitor.visitar_tunel(self)

    # --- Comportamiento ---
    def entrar(self, alguien):
        if self.laberinto is None:
            # Proxy Virtual: clonar el laberinto del juego al primer acceso
            self.laberinto = alguien.juego.clonar()
        self.laberinto.entrar(alguien)

    def es_tunel(self):
        return True

    def __str__(self):
        return "Tunel"


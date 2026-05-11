# Visitor: clase base del patron Visitor para recorrer el laberinto


class Visitor:
    """Visitor abstracto para recorrer los elementos del laberinto."""

    def visitar_habitacion(self, habitacion): pass
    def visitar_pared(self, pared):           pass
    def visitar_puerta(self, puerta):         pass
    def visitar_bomba(self, bomba):           pass
    def visitar_tunel(self, tunel):           pass
    def visitar_armario(self, armario):       pass

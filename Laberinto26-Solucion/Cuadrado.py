# Cuadrado: polígono regular de 4 lados (n, s, e, o)
from Forma import Forma


class Cuadrado(Forma):
    """Polígono de 4 lados. Almacena los ElementoMapa del norte, sur, este y oeste."""

    def __init__(self):
        super().__init__()
        # Slots para los elementos del mapa (paredes/puertas) en cada dirección
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    def __str__(self):
        return "Cuadrado"

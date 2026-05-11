# Rombo: polígono con orientaciones noreste, noroeste, sureste, suroeste
from Forma import Forma


class Rombo(Forma):
    """Polígono rombiforme. Almacena los ElementoMapa de ne, no, se y so."""

    def __init__(self):
        super().__init__()
        # Slots para los elementos del mapa en cada diagonal
        self.ne = None
        self.no = None
        self.se = None
        self.so = None

    def __str__(self):
        return "Rombo"

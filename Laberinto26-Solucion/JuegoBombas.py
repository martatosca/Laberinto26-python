from Juego import Juego
from ParedBomba import ParedBomba


class JuegoBombas(Juego):
    """JuegoBombas ilustra el patron FactoryMethod para crear laberintos con paredes-bomba."""

    def fabricar_pared(self):
        return ParedBomba()


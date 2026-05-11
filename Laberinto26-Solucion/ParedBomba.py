# ParedBomba: pared que tiene un comportamiento explosivo
from Pared import Pared


class ParedBomba(Pared):
    """ParedBomba ilustra el patron FactoryMethod para crear paredes con bombas."""

    def __init__(self):
        super().__init__()
        self.activa = False

    def entrar(self, alguien):
        print(f"{alguien} se ha chocado con una pared bomba")

    def __str__(self):
        return "ParedBomba"

# Dormido: modo de bicho que esta dormido (no ataca, duerme mucho)
import time
from Modo import Modo


class Dormido(Modo):
    """Modo Dormido: el bicho duerme 5 segundos y NO ataca.

    Patron: Strategy (nuevo ConcreteStrategy de Modo).
    Redefine 'duerme' para descansar mas tiempo y 'ataca' para no hacer nada,
    sin cambiar el diseño de Modo ni de Bicho.
    """

    def ataca(self, bicho):
        """El bicho dormido no ataca."""
        print(f"{bicho} esta dormido y no ataca")

    def duerme(self, bicho):
        print(f"{bicho} ronca profundamente...")
        time.sleep(5)

    def es_dormido(self):
        return True

    def __str__(self):
        return "Dormido"

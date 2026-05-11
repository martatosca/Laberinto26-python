# Agresivo: modo de bicho mas agresivo (duerme poco)
import time
from Modo import Modo


class Agresivo(Modo):
    """Modo agresivo: el bicho descansa solo 1 segundo entre acciones."""

    def duerme(self, bicho):
        print(f"{bicho} duerme")
        time.sleep(1)

    def es_agresivo(self):
        return True

    def __str__(self):
        return "Agresivo"

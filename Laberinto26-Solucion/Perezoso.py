# Perezoso: modo de bicho que se mueve poco (duerme mas)
import time
from Modo import Modo


class Perezoso(Modo):
    """Modo perezoso: el bicho descansa 3 segundos entre acciones."""

    def duerme(self, bicho):
        print(f"{bicho} duerme")
        time.sleep(3)

    def es_perezoso(self):
        return True

    def __str__(self):
        return "Perezoso"

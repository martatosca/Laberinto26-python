# Habitacion: es un Contenedor (elemento mapa)
from Contenedor import Contenedor


class Habitacion(Contenedor):
    """Habitacion es un Contenedor con forma asignada por el Builder (Bridge)."""

    def __init__(self, num=0):
        super().__init__()
        self.num = num

    # --- Visitor ---
    def aceptar_contenedor(self, visitor):
        visitor.visitar_habitacion(self)

    # --- Representacion ---
    def __str__(self):
        return f"Hab-{self.num}"


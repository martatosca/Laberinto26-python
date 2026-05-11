# Armario: Contenedor que tiene una puerta al este
from Contenedor import Contenedor


class Armario(Contenedor):
    """Armario es un Contenedor con forma asignada por el Builder.
    Tiene una puerta al este que comunica con el contenedor padre."""

    def __init__(self, num=0):
        super().__init__()
        self.num = num

    # --- Visitor ---
    def aceptar_contenedor(self, visitor):
        visitor.visitar_armario(self)

    # --- Consultas ---
    def es_armario(self):
        return True

    def __str__(self):
        return f"Armario-{self.num}"

# Decorator: Hoja que tiene (decora) un ElementoMapa
from Hoja import Hoja


class Decorator(Hoja):
    """Es-una Hoja que tiene-un (decora) ElementoMapa. Patron Decorator."""

    def __init__(self, em=None):
        super().__init__()
        self.em = em

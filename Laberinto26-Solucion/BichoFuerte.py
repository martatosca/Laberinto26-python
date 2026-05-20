# BichoFuerte: bicho con el doble de poder y mas vidas
from Bicho import Bicho


class BichoFuerte(Bicho):
    """BichoFuerte es una subclase de Bicho (patron Composite, elemento nuevo).

    Patron: Composite (nuevo tipo de Ente/Bicho sin variar el diseño).
    Nace con el doble de poder y el doble de vidas que un bicho normal,
    y avisa al atacar para que el jugador sepa que es peligroso.
    """

    def __init__(self):
        super().__init__()
        self.vidas = 100   # el doble que un Bicho normal (50)
        self.poder = 10    # hace 10 de daño por ataque

    def es_atacado_por(self, alguien):
        print(f"{self} es un bicho fuerte! Tiene {self.vidas} vidas")
        super().es_atacado_por(alguien)

    def __str__(self):
        return f"BichoFuerte-{self.modo}"
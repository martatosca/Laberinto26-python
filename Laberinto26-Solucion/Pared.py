# Pared: elemento del mapa que no se puede atravesar
from Hoja import Hoja


class Pared(Hoja):
    """Pared es un elemento del mapa que bloquea el paso."""

    def aceptar(self, visitor):
        visitor.visitar_pared(self)

    def entrar(self, alguien):
        print(f"{alguien} se ha chocado con una pared")

    def __str__(self):
        return "Pared"

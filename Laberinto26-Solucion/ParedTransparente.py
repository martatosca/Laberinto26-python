# ParedTransparente: pared que se puede "ver" pero no atravesar
from Pared import Pared


class ParedTransparente(Pared):
    """ParedTransparente es una subclase de Pared (patron Composite, Hoja nueva).

    Patron: Composite (Hoja nueva que hereda de Pared, sin variar el diseño).
    Se puede ver a traves de ella (informa de lo que hay al otro lado)
    pero sigue bloqueando el paso igual que una Pared normal.
    """

    def __init__(self):
        super().__init__()
        self.descripcion_otro_lado = "nada especial"  # texto descriptivo del otro lado

    def aceptar(self, visitor):
        visitor.visitar_pared_transparente(self)

    def entrar(self, alguien):
        print(f"{alguien} se choca con una pared transparente")
        print(f"  Puedes ver al otro lado: {self.descripcion_otro_lado}")
        print(f"  Pero no puedes pasar")

    def es_pared_transparente(self):
        return True

    def __str__(self):
        return "ParedTransparente"

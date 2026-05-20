# Escalera: elemento del mapa que lleva a otra habitacion
from Hoja import Hoja


class Escalera(Hoja):
    """Escalera es una Hoja (patron Composite) que transporta al ente
    a una habitacion destino cuando entra en ella.

    Patron: Composite (Hoja nueva, sin variar el diseño existente).
    Se configura con un destino (Contenedor) al que se teletransporta el ente.
    """

    def __init__(self):
        super().__init__()
        self.destino = None   # Contenedor (habitacion) al que lleva la escalera

    def aceptar(self, visitor):
        visitor.visitar_escalera(self)

    def entrar(self, alguien):
        # Lazy resolution: si el destino no esta seteado pero hay un num, resolverlo
        if self.destino is None and hasattr(self, '_destino_num') and self._destino_num is not None:
            juego = getattr(alguien, 'juego', None)
            if juego is not None:
                self.destino = juego.obtener_habitacion(self._destino_num)
        if self.destino is not None:
            print(f"{alguien} sube/baja la escalera hacia {self.destino}")
            self.destino.entrar(alguien)
        else:
            print(f"{alguien} encuentra una escalera pero no lleva a ningún sitio")

    def es_escalera(self):
        return True

    def __str__(self):
        dest = str(self.destino) if self.destino else "ninguno"
        return f"Escalera(destino={dest})"

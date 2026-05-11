from Visitor import Visitor


class VisitorCerrarPuertas(Visitor):
    """Visitor que cierra todas las puertas del laberinto."""

    def visitar_puerta(self, puerta):
        puerta.cerrar()

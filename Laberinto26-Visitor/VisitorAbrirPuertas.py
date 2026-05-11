from Visitor import Visitor


class VisitorAbrirPuertas(Visitor):
    """Visitor que abre todas las puertas del laberinto."""

    def visitar_puerta(self, puerta):
        puerta.abrir()

# Bicho: representa a los enemigos del personaje
from Ente import Ente


class Bicho(Ente):
    """Bicho es un Ente con un Modo de comportamiento (Strategy)."""

    def __init__(self):
        super().__init__()
        self.modo = None

    def actua(self):
        """Ejecuta la secuencia de acciones segun su modo."""
        self.modo.actua(self)

    def buscar_enemigo(self):
        """Pide al juego el personaje en su misma posicion."""
        return self.juego.buscar_personaje(self)

    def es_agresivo(self):
        return self.modo.es_agresivo()

    def es_perezoso(self):
        return self.modo.es_perezoso()

    def obtener_orientacion_aleatoria(self):
        return self.posicion.obtener_orientacion_aleatoria()

    def muero(self):
        self.juego.muere_bicho(self)

    def __str__(self):
        return f"Bicho-{self.modo}"

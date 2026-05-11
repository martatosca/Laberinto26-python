# Ente: interfaz de los elementos autonomos del laberinto


class Ente:
    """Ente es la interfaz de personajes y bichos del laberinto."""

    def __init__(self):
        self.vidas = 50
        self.poder = 1
        self.posicion = None
        self.juego = None

    # --- Ataques ---
    def atacar(self):
        """Busca un enemigo y lo ataca."""
        enemigo = self.buscar_enemigo()
        if enemigo is not None:
            enemigo.es_atacado_por(self)

    def buscar_enemigo(self):
        """Metodo abstracto: cada subclase sabe como buscar su enemigo."""
        raise NotImplementedError

    def es_atacado_por(self, alguien):
        """Recibe dano de alguien y comprueba si muere."""
        self.vidas = self.vidas - alguien.poder
        print(f"{self} es atacado por {alguien}")
        print(f"vidas: {self.vidas}")
        if self.vidas <= 0:
            self.vidas = 0
            self.muero()

    def esta_vivo(self):
        return self.vidas > 0

    def muero(self):
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__

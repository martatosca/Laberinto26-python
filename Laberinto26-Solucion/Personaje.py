# Personaje: el protagonista del juego
# Extendido con inventario para la extension Media
from Ente import Ente


class Personaje(Ente):
    """Personaje es el protagonista del juego del laberinto.

    Extension Media: se anade un inventario (lista de objetos recogidos)
    que permite interactuar con Llaves y PuertasSalida.
    """

    def __init__(self):
        super().__init__()
        self.nombre = ""
        self.inventario = []   # NUEVO: lista de objetos recogidos (Llaves, etc.)

    def buscar_enemigo(self):
        return self.juego.buscar_bicho()

    def ir_a(self, orientacion):
        orientacion.caminar(self)

    def ir_al_norte(self):
        from Orientaciones import Norte
        Norte().caminar(self)

    def coger_llave(self):
        """Intenta recoger una llave en la habitacion actual."""
        hab = self.posicion
        llave = None
        for hijo in hab.hijos:
            if hijo.es_llave() and not hijo.recogida:
                llave = hijo
                break
        if llave:
            llave.entrar(self)
        else:
            print(f"No hay ninguna llave que recoger en {hab}")

    def tiene_llave(self):
        return any(item.es_llave() for item in self.inventario)

    def muero(self):
        self.juego.muere_personaje()

    def __str__(self):
        return self.nombre

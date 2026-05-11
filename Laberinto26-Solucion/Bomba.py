# Bomba: elemento del mapa que puede explotar si esta activa
from Decorator import Decorator


class Bomba(Decorator):
    """Bomba es un Decorator que puede explotar cuando alguien entra."""

    def __init__(self):
        super().__init__()
        self.activa = False

    def aceptar(self, visitor):
        visitor.visitar_bomba(self)

    def activar(self):
        print("Bomba activada")
        self.activa = True

    def desactivar(self):
        print("Bomba desactivada")
        self.activa = False

    def es_bomba(self):
        return True

    def entrar(self, alguien):
        if self.activa:
            print(f"{alguien}, te ha explotado una bomba")
            # TODO: quitar vidas a alguien

    def __str__(self):
        return "Bomba"

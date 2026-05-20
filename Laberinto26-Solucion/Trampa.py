# Trampa: elemento del mapa que daña al que entra
from Hoja import Hoja


class Trampa(Hoja):
    """Trampa es una Hoja (patron Composite) que quita vidas a quien entre en ella.
    
    Patron: Composite (Hoja nueva, sin variar el diseño existente).
    Al entrar, reduce las vidas del ente en la cantidad de 'danio'.
    """

    def __init__(self, danio=10):
        super().__init__()
        self.danio = danio   # puntos de vida que quita al entrar

    def aceptar(self, visitor):
        visitor.visitar_trampa(self)

    def entrar(self, alguien):
        print(f"{alguien} ha caido en una trampa y pierde {self.danio} vidas")
        alguien.vidas -= self.danio
        print(f"Vidas restantes de {alguien}: {alguien.vidas}")
        if alguien.vidas <= 0:
            alguien.vidas = 0
            alguien.muero()

    def es_trampa(self):
        return True

    def __str__(self):
        return f"Trampa(danio={self.danio})"

# Llave: elemento del mapa que el personaje puede recoger
from Hoja import Hoja


class Llave(Hoja):
    """Llave es una Hoja (patron Composite) que el personaje puede recoger
    para desbloquear una PuertaSalida.

    Patron principal: Composite (Hoja nueva).
    Patron secundario: interactua con el Inventario del Personaje.

    Al entrar, la llave se anade al inventario del personaje y se elimina
    de los hijos de la habitacion donde estaba.
    """

    def __init__(self):
        super().__init__()
        self.recogida = False

    def aceptar(self, visitor):
        visitor.visitar_llave(self)

    def entrar(self, alguien):
        if self.recogida:
            print("La llave ya ha sido recogida")
            return
        if hasattr(alguien, 'inventario'):
            alguien.inventario.append(self)
            self.recogida = True
            print(f"¡{alguien} ha recogido una llave! Ahora tiene {len(alguien.inventario)} objeto(s) en su inventario")
        else:
            print(f"{alguien} no puede recoger objetos")

    def es_llave(self):
        return True

    def __str__(self):
        estado = "recogida" if self.recogida else "disponible"
        return f"Llave({estado})"

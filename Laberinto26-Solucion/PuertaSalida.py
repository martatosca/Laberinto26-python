# PuertaSalida: puerta especial que comienza bloqueada
from Puerta import Puerta
from EstadoPuerta import Bloqueada


class PuertaSalida(Puerta):
    """PuertaSalida es una Puerta (patron Composite + State) que comienza
    en estado Bloqueada en lugar de Cerrada.

    Patron: State (usa el nuevo estado Bloqueada).
    Solo se puede abrir si el personaje lleva una Llave en su inventario.
    """

    def __init__(self):
        super().__init__()
        self.estado = Bloqueada()   # sobreescribe el Cerrada() del padre

    def es_puerta_salida(self):
        return True

    def __str__(self):
        n1 = self.lado1.num if self.lado1 else "?"
        n2 = self.lado2.num if self.lado2 else "?"
        return f"PuertaSalida-{n1}-{n2}[{self.estado}]"

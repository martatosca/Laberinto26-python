# Puerta: elemento del mapa que une dos habitaciones
from Hoja import Hoja
from EstadoPuerta import EstadoPuerta, Abierta, Cerrada


class Puerta(Hoja):
    """Puerta une dos contenedores y tiene un estado (patron State).
    Por defecto comienza cerrada."""

    def __init__(self):
        super().__init__()
        self.lado1 = None
        self.lado2 = None
        self.estado = Cerrada()

    # --- Visitor ---
    def aceptar(self, visitor):
        visitor.visitar_puerta(self)

    # --- State ---
    def abrir(self):
        """Delega la accion abrir al estado actual."""
        self.estado.abrir(self)

    def cerrar(self):
        """Delega la accion cerrar al estado actual."""
        self.estado.cerrar(self)

    def entrar(self, alguien):
        """Delega la entrada al estado actual."""
        self.estado.entrar(alguien, self)

    def puede_entrar(self, alguien):
        """Calcula a que lado debe ir alguien y lo mueve."""
        if alguien.posicion == self.lado1:
            self.lado2.entrar(alguien)
        else:
            self.lado1.entrar(alguien)

    # --- Consultas ---
    def es_puerta(self):
        return True

    def esta_abierta(self):
        return self.estado.esta_abierta()

    def esta_cerrada(self):
        return self.estado.esta_cerrada()

    def __str__(self):
        n1 = self.lado1.num if self.lado1 else "?"
        n2 = self.lado2.num if self.lado2 else "?"
        return f"Puerta-{n1}-{n2}"

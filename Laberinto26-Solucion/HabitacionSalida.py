# HabitacionSalida: habitacion especial que termina el juego con victoria
from Habitacion import Habitacion


class HabitacionSalida(Habitacion):
    """HabitacionSalida es una Habitacion especial (patron Composite,
    nuevo tipo de Contenedor) que representa la salida del laberinto.

    Patron: Composite (nuevo Contenedor).
    Al entrar en ella, se comprueba si el personaje lleva una llave;
    si es asi, el juego termina con victoria del personaje.
    """

    def __init__(self, num=0):
        super().__init__(num)

    def entrar(self, alguien):
        alguien.posicion = self
        if alguien.juego is not None:
            alguien.juego.gana_personaje()

    def __str__(self):
        return f"HabitacionSalida-{self.num}"

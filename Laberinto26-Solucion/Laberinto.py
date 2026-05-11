# Laberinto es un Contenedor que tiene habitaciones
from Contenedor import Contenedor
from Forma import Forma


class _FormaVacia(Forma):
    """Forma sin orientaciones usada internamente por Laberinto."""
    def __init__(self):
        super().__init__()


class Laberinto(Contenedor):
    """Laberinto: contenedor raiz que agrupa las habitaciones."""

    def __init__(self):
        super().__init__()
        # Laberinto usa una forma vacia (no tiene lados propios)
        self.forma = _FormaVacia()

    # --- Visitor ---
    def aceptar_contenedor(self, visitor):
        pass  # Laberinto no necesita ser visitado a si mismo

    def aceptar(self, visitor):
        """Visita cada habitacion hijo."""
        for hab in self.hijos:
            hab.aceptar(visitor)

    # --- Gestion de habitaciones ---
    def agregar_habitacion(self, hab):
        """Anade una habitacion al laberinto."""
        self.agregar_hijo(hab)

    def obtener_habitacion(self, num):
        """Devuelve la habitacion con el numero indicado, o None."""
        for hab in self.hijos:
            if hab.num == num:
                return hab
        return None

    def numero_habitaciones(self):
        return len(self.hijos)

    # --- Comportamiento ---
    def entrar(self, alguien):
        """Entra al laberinto: lleva al ente a la habitacion 1."""
        print(f"{alguien} ha entrado en el laberinto")
        hab = self.obtener_habitacion(1)
        if hab:
            hab.entrar(alguien)

    def recorrer(self, bloque):
        """Recorre todas las habitaciones aplicando el bloque."""
        print("Recorriendo el laberinto")
        for hab in self.hijos:
            hab.recorrer(bloque)

    def __str__(self):
        return f"Laberinto-{self.num}"


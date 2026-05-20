# EstadoPuerta: interfaz de los estados de la puerta (patron State)
# Extendido con el estado Bloqueada para la extension Media 2
from abc import ABC, abstractmethod


class EstadoPuerta(ABC):
    """Interfaz del patron State para el estado de una Puerta."""

    def abrir(self, puerta):        pass
    def cerrar(self, puerta):       pass
    def desbloquear(self, puerta):  pass

    @abstractmethod
    def entrar(self, alguien, puerta):
        pass

    def esta_abierta(self):     return False
    def esta_cerrada(self):     return False
    def esta_bloqueada(self):   return False


class Abierta(EstadoPuerta):
    """Estado Abierta: se puede pasar y se puede cerrar."""

    def cerrar(self, puerta):
        print(f"Cerramos {puerta}")
        puerta.estado = Cerrada()

    def entrar(self, alguien, puerta):
        puerta.puede_entrar(alguien)

    def esta_abierta(self):
        return True

    def __str__(self):
        return "Abierta"


class Cerrada(EstadoPuerta):
    """Estado Cerrada: no se puede pasar pero se puede abrir."""

    def abrir(self, puerta):
        print(f"Abrimos {puerta}")
        puerta.estado = Abierta()

    def entrar(self, alguien, puerta):
        print(f"La puerta {puerta} esta cerrada. Intenta abrirla.")

    def esta_cerrada(self):
        return True

    def __str__(self):
        return "Cerrada"


class Bloqueada(EstadoPuerta):
    """Estado Bloqueada (NUEVA - Extension Media 2): la puerta solo se puede
    desbloquear si el personaje lleva una Llave en su inventario.

    Patron: State. Tercer estado de EstadoPuerta que comprueba el inventario
    del personaje antes de permitir la transicion a Abierta.
    """

    def desbloquear(self, puerta):
        print(f"Desbloqueamos {puerta}")
        puerta.estado = Abierta()

    def entrar(self, alguien, puerta):
        if hasattr(alguien, 'inventario') and any(item.es_llave() for item in alguien.inventario):
            print(f"¡{alguien} usa la llave para desbloquear {puerta}!")
            # Consume la llave del inventario
            llave = next(item for item in alguien.inventario if item.es_llave())
            alguien.inventario.remove(llave)
            self.desbloquear(puerta)
            puerta.puede_entrar(alguien)
        else:
            print(f"¡{puerta} está bloqueada! Necesitas una llave para pasar.")

    def esta_bloqueada(self):
        return True

    def __str__(self):
        return "Bloqueada"

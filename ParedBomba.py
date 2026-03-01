from Pared import Pared
#es subclase de pared, pero tiene una bomba que se activa al entrar en la habitación
class ParedBomba(Pared):
    def __init__(self, activa=True):
        super().__init__()
        self.activa = activa

    def entrar(self):
        if self.activa:
            print("BOOM! La pared bomba ha explotado.")
        else:
            print("Es una pared bomba desactivada.")

    def __str__(self):
        estado = "activa" if self.activa else "desactivada"
        return f"ParedBomba ({estado})"
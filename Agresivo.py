from Modo import Modo

class Agresivo(Modo):
    """
    ConcreteStrategy: Modo agresivo.
    El bicho ataca y persigue al jugador.
    """
    
    def actuar(self, bicho) -> str:
        mensaje = f"{bicho.nombre} está en modo AGRESIVO: ¡Ataca ferozmente!"
        print(mensaje)
        return mensaje
    
    def obtener_nombre(self) -> str:
        return "Agresivo"

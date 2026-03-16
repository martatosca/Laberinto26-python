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
    
    def caminar(self, bicho) -> str:
        mensaje = f"{bicho.nombre} corre rápidamente buscando enemigos"
        print(mensaje)
        return mensaje
    
    def atacar(self, bicho) -> str:
        mensaje = f"{bicho.nombre} ataca con furia! Daño: {bicho.poder * 2}"
        print(mensaje)
        return mensaje
    
    def dormir(self, bicho) -> str:
        mensaje = f"{bicho.nombre} duerme con un ojo abierto, alerta"
        print(mensaje)
        return mensaje
    
    def obtener_nombre(self) -> str:
        return "Agresivo"

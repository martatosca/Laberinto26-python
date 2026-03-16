from Modo import Modo

class Agresivo(Modo):
    """
    ConcreteClass del patrón Template Method.
    Modo agresivo: especializado en ATACAR.
    Redefine atacar() con comportamiento potenciado.
    """
    
    # ==================== OPERACIONES PRIMITIVAS ====================
    def atacar(self, bicho) -> str:
        """Operación primitiva ESPECIALIZADA: El agresivo ataca con furia"""
        mensaje = f"  -> {bicho.nombre} ¡ATACA CON FURIA! Daño: {bicho.poder * 2}"
        print(mensaje)
        return mensaje
    
    def duerme(self, bicho) -> str:
        """Operación primitiva básica: duerme alerta"""
        mensaje = f"  -> {bicho.nombre} duerme con un ojo abierto, alerta"
        print(mensaje)
        return mensaje
    
    # ==================== OTROS MÉTODOS ====================
    def caminar(self, bicho) -> str:
        mensaje = f"{bicho.nombre} corre rápidamente buscando enemigos"
        print(mensaje)
        return mensaje
    
    def obtener_nombre(self) -> str:
        return "Agresivo"

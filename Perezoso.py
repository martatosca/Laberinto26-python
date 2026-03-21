from Modo import Modo

class Perezoso(Modo):
    """
    ConcreteClass del patrón Template Method.
    Modo perezoso: especializado en DORMIR.
    Redefine duerme() con comportamiento potenciado.
    """
    
    # ==================== OPERACIONES PRIMITIVAS ====================
    def atacar(self, bicho) -> str:
        """Operación primitiva básica: ataca sin ganas"""
        mensaje = f"  -> {bicho.nombre} ataca sin ganas... Daño: {bicho.poder // 2}"
        print(mensaje)
        return mensaje
    
    def duerme(self, bicho) -> str:
        """Operación primitiva ESPECIALIZADA: El perezoso duerme profundamente"""
        mensaje = f"  -> {bicho.nombre} ¡DUERME PROFUNDAMENTE! Ronquidos ensordecedores..."
        print(mensaje)
        return mensaje
    
    # ==================== OTROS MÉTODOS ====================
    def caminar(self, bicho) -> str:
        mensaje = f"{bicho.nombre} camina muy lentamente, arrastrando los pies"
        print(mensaje)
        return mensaje
    
    def obtener_nombre(self) -> str:
        return "Perezoso"
    
    def cambiar_modo(self, bicho):
        """
        Adapter: Cambia de Perezoso a Agresivo.
        """
        from Agresivo import Agresivo
        nuevo_modo = Agresivo()
        bicho.modo = nuevo_modo
        print(f"  ✨ {bicho.nombre} cambia de Perezoso a Agresivo")
        return nuevo_modo

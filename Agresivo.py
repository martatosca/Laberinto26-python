from Modo import Modo

class Agresivo(Modo):
    
    
    def atacar(self, bicho) -> str:
        
        mensaje = f"  -> {bicho.nombre} ¡ATACA CON FURIA! Daño: {bicho.poder * 2}"
        print(mensaje)
        return mensaje
    
    def duerme(self, bicho) -> str:
        
        mensaje = f"  -> {bicho.nombre} duerme con un ojo abierto, alerta"
        print(mensaje)
        return mensaje
    
    def caminar(self, bicho) -> str:
        mensaje = f"{bicho.nombre} corre rápidamente buscando enemigos"
        print(mensaje)
        return mensaje
    
    def obtener_nombre(self) -> str:
        return "Agresivo"
    
    def cambiar_modo(self, bicho):
        
        from Perezoso import Perezoso
        nuevo_modo = Perezoso()
        bicho.modo = nuevo_modo
        print(f"  ✨ {bicho.nombre} cambia de Agresivo a Perezoso")
        return nuevo_modo

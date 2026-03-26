from Modo import Modo

class Perezoso(Modo):
    
    
    def atacar(self, bicho) -> str:
        
        mensaje = f"  -> {bicho.nombre} ataca sin ganas... Daño: {bicho.poder // 2}"
        print(mensaje)
        return mensaje
    
    def duerme(self, bicho) -> str:
        
        mensaje = f"  -> {bicho.nombre} ¡DUERME PROFUNDAMENTE! Ronquidos ensordecedores..."
        print(mensaje)
        return mensaje
    
    def caminar(self, bicho) -> str:
        mensaje = f"{bicho.nombre} camina muy lentamente, arrastrando los pies"
        print(mensaje)
        return mensaje
    
    def obtener_nombre(self) -> str:
        return "Perezoso"
    
    def cambiar_modo(self, bicho):
        
        from Agresivo import Agresivo
        nuevo_modo = Agresivo()
        bicho.modo = nuevo_modo
        print(f"  ✨ {bicho.nombre} cambia de Perezoso a Agresivo")
        return nuevo_modo

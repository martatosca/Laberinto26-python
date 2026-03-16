from Modo import Modo

class Perezoso(Modo):
    """
    ConcreteStrategy: Modo perezoso.
    El bicho se mueve lentamente y no ataca.
    """
    
    def actuar(self, bicho) -> str:
        mensaje = f"{bicho.nombre} está en modo PEREZOSO: Se mueve lentamente..."
        print(mensaje)
        return mensaje
    
    def caminar(self, bicho) -> str:
        mensaje = f"{bicho.nombre} camina muy lentamente, arrastrando los pies"
        print(mensaje)
        return mensaje
    
    def atacar(self, bicho) -> str:
        mensaje = f"{bicho.nombre} ataca sin ganas... Daño: {bicho.poder // 2}"
        print(mensaje)
        return mensaje
    
    def dormir(self, bicho) -> str:
        mensaje = f"{bicho.nombre} duerme profundamente, roncando"
        print(mensaje)
        return mensaje
    
    def obtener_nombre(self) -> str:
        return "Perezoso"

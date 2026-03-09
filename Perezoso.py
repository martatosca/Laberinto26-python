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
    
    def obtener_nombre(self) -> str:
        return "Perezoso"

from Orientacion import Orientacion

class Norte(Orientacion):
    """ConcreteStrategy: Orientación Norte"""
    
    def obtener_nombre(self) -> str:
        return "Norte"
    
    def obtener_opuesta(self) -> Orientacion:
        return Sur()


class Sur(Orientacion):
    """ConcreteStrategy: Orientación Sur"""
    
    def obtener_nombre(self) -> str:
        return "Sur"
    
    def obtener_opuesta(self) -> Orientacion:
        return Norte()


class Este(Orientacion):
    """ConcreteStrategy: Orientación Este"""
    
    def obtener_nombre(self) -> str:
        return "Este"
    
    def obtener_opuesta(self) -> Orientacion:
        return Oeste()


class Oeste(Orientacion):
    """ConcreteStrategy: Orientación Oeste"""
    
    def obtener_nombre(self) -> str:
        return "Oeste"
    
    def obtener_opuesta(self) -> Orientacion:
        return Este()

from Orientacion import Orientacion

class Norte(Orientacion):
    """
    ConcreteStrategy + Singleton: Orientación Norte.
    Solo existe una instancia de Norte en todo el programa.
    """
    _unicaInstancia = None  # Singleton: única instancia
    
    def __new__(cls):
        """Singleton: retorna siempre la misma instancia"""
        if cls._unicaInstancia is None:
            cls._unicaInstancia = super().__new__(cls)
        return cls._unicaInstancia
    
    def obtener_nombre(self) -> str:
        return "Norte"
    
    def obtener_opuesta(self) -> Orientacion:
        return Sur()  # Retorna el Singleton de Sur


class Sur(Orientacion):
    """
    ConcreteStrategy + Singleton: Orientación Sur.
    Solo existe una instancia de Sur en todo el programa.
    """
    _unicaInstancia = None  # Singleton: única instancia
    
    def __new__(cls):
        """Singleton: retorna siempre la misma instancia"""
        if cls._unicaInstancia is None:
            cls._unicaInstancia = super().__new__(cls)
        return cls._unicaInstancia
    
    def obtener_nombre(self) -> str:
        return "Sur"
    
    def obtener_opuesta(self) -> Orientacion:
        return Norte()  # Retorna el Singleton de Norte


class Este(Orientacion):
    """
    ConcreteStrategy + Singleton: Orientación Este.
    Solo existe una instancia de Este en todo el programa.
    """
    _unicaInstancia = None  # Singleton: única instancia
    
    def __new__(cls):
        """Singleton: retorna siempre la misma instancia"""
        if cls._unicaInstancia is None:
            cls._unicaInstancia = super().__new__(cls)
        return cls._unicaInstancia
    
    def obtener_nombre(self) -> str:
        return "Este"
    
    def obtener_opuesta(self) -> Orientacion:
        return Oeste()  # Retorna el Singleton de Oeste


class Oeste(Orientacion):
    """
    ConcreteStrategy + Singleton: Orientación Oeste.
    Solo existe una instancia de Oeste en todo el programa.
    """
    _unicaInstancia = None  # Singleton: única instancia
    
    def __new__(cls):
        """Singleton: retorna siempre la misma instancia"""
        if cls._unicaInstancia is None:
            cls._unicaInstancia = super().__new__(cls)
        return cls._unicaInstancia
    
    def obtener_nombre(self) -> str:
        return "Oeste"
    
    def obtener_opuesta(self) -> Orientacion:
        return Este()  # Retorna el Singleton de Este

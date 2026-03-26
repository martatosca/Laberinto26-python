from Orientacion import Orientacion

class Norte(Orientacion):
    
    _unicaInstancia = None
    
    def __new__(cls):
        
        if cls._unicaInstancia is None:
            cls._unicaInstancia = super().__new__(cls)
        return cls._unicaInstancia
    
    def obtener_nombre(self) -> str:
        return "Norte"
    
    def obtener_opuesta(self) -> Orientacion:
        return Sur()

class Sur(Orientacion):
    
    _unicaInstancia = None
    
    def __new__(cls):
        
        if cls._unicaInstancia is None:
            cls._unicaInstancia = super().__new__(cls)
        return cls._unicaInstancia
    
    def obtener_nombre(self) -> str:
        return "Sur"
    
    def obtener_opuesta(self) -> Orientacion:
        return Norte()

class Este(Orientacion):
    
    _unicaInstancia = None
    
    def __new__(cls):
        
        if cls._unicaInstancia is None:
            cls._unicaInstancia = super().__new__(cls)
        return cls._unicaInstancia
    
    def obtener_nombre(self) -> str:
        return "Este"
    
    def obtener_opuesta(self) -> Orientacion:
        return Oeste()

class Oeste(Orientacion):
    
    _unicaInstancia = None
    
    def __new__(cls):
        
        if cls._unicaInstancia is None:
            cls._unicaInstancia = super().__new__(cls)
        return cls._unicaInstancia
    
    def obtener_nombre(self) -> str:
        return "Oeste"
    
    def obtener_opuesta(self) -> Orientacion:
        return Este()

class Noreste(Orientacion):
    
    _unicaInstancia = None
    
    def __new__(cls):
        if cls._unicaInstancia is None:
            cls._unicaInstancia = super().__new__(cls)
        return cls._unicaInstancia
    
    def obtener_nombre(self) -> str:
        return "Noreste"
    
    def obtener_opuesta(self) -> Orientacion:
        return Suroeste()

class Noroeste(Orientacion):
    
    _unicaInstancia = None
    
    def __new__(cls):
        if cls._unicaInstancia is None:
            cls._unicaInstancia = super().__new__(cls)
        return cls._unicaInstancia
    
    def obtener_nombre(self) -> str:
        return "Noroeste"
    
    def obtener_opuesta(self) -> Orientacion:
        return Sureste()

class Sureste(Orientacion):
    
    _unicaInstancia = None
    
    def __new__(cls):
        if cls._unicaInstancia is None:
            cls._unicaInstancia = super().__new__(cls)
        return cls._unicaInstancia
    
    def obtener_nombre(self) -> str:
        return "Sureste"
    
    def obtener_opuesta(self) -> Orientacion:
        return Noroeste()

class Suroeste(Orientacion):
    
    _unicaInstancia = None
    
    def __new__(cls):
        if cls._unicaInstancia is None:
            cls._unicaInstancia = super().__new__(cls)
        return cls._unicaInstancia
    
    def obtener_nombre(self) -> str:
        return "Suroeste"
    
    def obtener_opuesta(self) -> Orientacion:
        return Noreste()

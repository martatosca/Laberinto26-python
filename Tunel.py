from Hoja import Hoja

class Tunel(Hoja):
    
    
    def __init__(self, laberinto=None):
        super().__init__()
        self._laberinto = laberinto
    
    @property
    def laberinto(self):
        
        return self._laberinto
    
    @laberinto.setter
    def laberinto(self, value):
        
        self._laberinto = value
    
    def entrar(self, alguien=None):
        
        if self._laberinto is None:
            print("El túnel no lleva a ningún sitio...")
            return
        
        if alguien:
            print(f"{alguien} entra en el túnel...")
            print(f"¡{alguien} es transportado a {self._laberinto}!")
            primera_hab = self._laberinto.obtener_primera_habitacion()
            if primera_hab:
                primera_hab.entrar(alguien)
            else:
                self._laberinto.entrar()
        else:
            print("Entras en el túnel...")
            print(f"¡Has sido transportado a {self._laberinto}!")
            self._laberinto.entrar()
    
    def recorrer(self):
        
        yield self
        if self._laberinto:
            yield from self._laberinto.recorrer()
    
    def __str__(self):
        if self._laberinto:
            return f"Tunel -> {self._laberinto}"
        return "Tunel (sin destino)"

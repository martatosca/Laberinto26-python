from Hoja import Hoja

class Tunel(Hoja):
    """
    PROXY del patrón Proxy.
    
    El Tunel actúa como un sustituto del Laberinto al que conecta.
    Cuando alguien entra en el Tunel, es transportado a otro laberinto.
    
    - Subject: ElementoMapa (interfaz común)
    - RealSubject: Laberinto (el objeto real al que el proxy da acceso)
    - Proxy: Tunel (mantiene referencia al laberinto y controla acceso)
    
    Responsabilidades del Proxy:
    - Mantiene referencia al laberinto destino (+laberinto)
    - Proporciona la misma interfaz que ElementoMapa (entrar, recorrer)
    - Controla el acceso al laberinto (puede crearlo bajo demanda)
    """
    
    def __init__(self, laberinto=None):
        super().__init__()
        self._laberinto = laberinto  # Referencia al RealSubject
    
    @property
    def laberinto(self):
        """Obtiene el laberinto destino (RealSubject)"""
        return self._laberinto
    
    @laberinto.setter
    def laberinto(self, value):
        """Establece el laberinto destino"""
        self._laberinto = value
    
    def entrar(self, alguien=None):
        """
        Proxy: Controla el acceso al laberinto.
        Cuando alguien entra al túnel, es transportado al laberinto destino.
        """
        if self._laberinto is None:
            print("El túnel no lleva a ningún sitio...")
            return
        
        if alguien:
            print(f"{alguien} entra en el túnel...")
            print(f"¡{alguien} es transportado a {self._laberinto}!")
            # Delega al RealSubject: entra en la primera habitación del laberinto
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
        """
        Proxy: Recorre el túnel y luego delega al laberinto.
        """
        yield self
        if self._laberinto:
            yield from self._laberinto.recorrer()
    
    def __str__(self):
        if self._laberinto:
            return f"Tunel -> {self._laberinto}"
        return "Tunel (sin destino)"

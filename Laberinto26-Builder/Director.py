import json
from LaberintoBuilder import LaberintoBuilder
from LaberintoBuilderRombo import LaberintoBuilderRombo


class Director:
    """Dirige el proceso de construccion del laberinto usando un Builder."""

    def __init__(self):
        self._builder = None
        self._dict = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, value):
        self._builder = value

    @property
    def dict(self):
        return self._dict

    def obtener_juego(self):
        """Devuelve el Juego construido por el Builder."""
        return self._builder.juego

    # ------------------------------------------------------------------
    # Punto de entrada principal
    # ------------------------------------------------------------------

    def procesar(self, archivo: str):
        """Lee el JSON, construye el laberinto y devuelve el Juego listo."""
        self.leer_archivo(archivo)
        self.ini_builder()
        self.fabricar_laberinto()
        self.fabricar_juego()
        self.fabricar_bichos()

    # ------------------------------------------------------------------
    # Pasos de construccion
    # ------------------------------------------------------------------

    def leer_archivo(self, archivo: str):
        with open(archivo, 'r', encoding='utf-8') as f:
            self._dict = json.load(f)

    def ini_builder(self):
        forma = self._dict.get('forma', 'poligono4')
        if forma == 'rombo':
            self._builder = LaberintoBuilderRombo()
        else:
            self._builder = LaberintoBuilder()

    def fabricar_laberinto(self):
        self._builder.fabricar_laberinto()

        laberinto_data = self._dict.get('laberinto', [])
        for elem in laberinto_data:
            self._fabricar_recursivo(elem, None)

        puertas_data = self._dict.get('puertas', [])
        for puerta in puertas_data:
            self._builder.fabricar_puerta_lado1_or1_lado2_or2(
                puerta[0], puerta[1], puerta[2], puerta[3])

    def fabricar_juego(self):
        self._builder.fabricar_juego()

    def fabricar_bichos(self):
        bichos_data = self._dict.get('bichos', [])
        for bicho_data in bichos_data:
            modo = bicho_data.get('modo', 'Agresivo')
            posicion = bicho_data.get('posicion', 1)
            self._builder.fabricar_bicho_modo(modo, posicion)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _fabricar_recursivo(self, dic: dict, padre):
        tipo = dic.get('tipo', '')
        contenedor = None

        if tipo == 'habitacion':
            contenedor = self._builder.fabricar_habitacion(dic.get('num', 0))

        elif tipo == 'armario':
            if padre is not None:
                contenedor = self._builder.fabricar_armario(dic.get('num', 0), padre)

        elif tipo == 'bomba':
            if padre is not None:
                self._builder.fabricar_bomba_en(padre)
            return

        elif tipo == 'tunel':
            if padre is not None:
                self._builder.fabricar_tunel_en(padre)
            return

        for hijo in dic.get('hijos', []):
            self._fabricar_recursivo(hijo, contenedor)

    def __str__(self):
        return f"Director con builder={self._builder}"


        
        if forma == 'poligono4':
            self._builder = LaberintoBuilder()
        else:
            self._builder = LaberintoBuilder()
    
    
    def fabricarLaberinto(self):
        
        self._builder.fabricarLaberinto()
        
        laberinto_data = self._dict.get('laberinto', [])
        for elem in laberinto_data:
            self.fabricarLaberintoRecursivo(elem, None)
        
        puertas_data = self._dict.get('puertas', [])
        for puerta in puertas_data:
            self._builder.fabricarPuertaLado1Or1Lado2Or2(
                puerta[0], puerta[1], puerta[2], puerta[3]
            )
    
    def fabricarLaberintoRecursivo(self, dic: dict, padre):
        
        tipo = dic.get('tipo', '')
        contenedor = None
        
        if tipo == 'habitacion':
            contenedor = self._builder.fabricarHabitacion(dic.get('num', 0))
        
        elif tipo == 'armario':
            if padre:
                contenedor = self._builder.fabricarArmario(dic.get('num', 0), padre)
        
        elif tipo == 'bomba':
            if padre:
                self._builder.fabricarBombaEn(padre)
            return
        
        hijos = dic.get('hijos', [])
        for hijo in hijos:
            self.fabricarLaberintoRecursivo(hijo, contenedor)
    
    
    def fabricarJuego(self):
        
        self._juego = Juego()
        self._juego.laberinto = self._builder.obtenerLaberinto()
        
        self._builder.juego = self._juego
    
    
    def fabricarBichos(self):
        
        bichos_data = self._dict.get('bichos', [])
        
        if not bichos_data:
            return
        
        for bicho_data in bichos_data:
            modo = bicho_data.get('modo', 'Agresivo')
            posicion = bicho_data.get('posicion', 1)
            self._builder.fabricarBichoModo(modo, posicion)
    
    def __str__(self):
        return f"Director con builder={self._builder}"

import json
from Builder import Builder
from LaberintoBuilder import LaberintoBuilder
from Juego_arreglar import Juego

class Director:
    
    
    def __init__(self):
        self._builder = None
        self._dict = None
        self._juego = None
    
    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, value: Builder):
        self._builder = value
    
    @property
    def dict(self):
        return self._dict
    
    @property
    def juego(self):
        return self._juego
    
    
    def procesar(self, archivo: str):
        
        self.leerArchivo(archivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()
        
        return self._juego
    
    
    def leerArchivo(self, archivo: str):
        
        with open(archivo, 'r', encoding='utf-8') as f:
            self._dict = json.load(f)
    
    
    def iniBuilder(self):
        
        forma = self._dict.get('forma', 'poligono4')
        
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

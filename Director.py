import json
from Builder import Builder
from LaberintoBuilder import LaberintoBuilder
from Juego_arreglar import Juego


class Director:
    """
    Director: Construye un objeto utilizando la interfaz del Builder.
    Orquesta el proceso de construcción del laberinto leyendo desde un archivo JSON.
    """
    
    def __init__(self):
        self._builder = None
        self._dict = None  # Diccionario con datos del JSON
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
    
    # ==================== PROCESO PRINCIPAL ====================
    
    def procesar(self, archivo: str):
        """
        Proceso principal que construye el laberinto desde un archivo JSON.
        Sigue la secuencia del código del profesor.
        """
        self.leerArchivo(archivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()
        
        return self._juego
    
    # ==================== LECTURA DE ARCHIVO ====================
    
    def leerArchivo(self, archivo: str):
        """Lee el archivo JSON y lo convierte a diccionario"""
        with open(archivo, 'r', encoding='utf-8') as f:
            self._dict = json.load(f)
    
    # ==================== INICIALIZACIÓN DEL BUILDER ====================
    
    def iniBuilder(self):
        """
        Inicializa el Builder según la 'forma' especificada en el JSON.
        Aquí podemos cambiar el Builder para crear laberintos diferentes.
        """
        forma = self._dict.get('forma', 'poligono4')
        
        if forma == 'poligono4':
            self._builder = LaberintoBuilder()
        # Aquí se pueden añadir más builders para otras formas
        else:
            self._builder = LaberintoBuilder()  # Por defecto
    
    # ==================== FABRICACIÓN DEL LABERINTO ====================
    
    def fabricarLaberinto(self):
        """
        Construye el laberinto usando el builder.
        1. Crea el laberinto vacío
        2. Crea habitaciones/armarios/bombas recursivamente
        3. Crea las puertas entre habitaciones
        """
        # Crear laberinto vacío
        self._builder.fabricarLaberinto()
        
        # Recorrer la estructura del laberinto y crear elementos recursivamente
        laberinto_data = self._dict.get('laberinto', [])
        for elem in laberinto_data:
            self.fabricarLaberintoRecursivo(elem, None)
        
        # Recorrer la colección de puertas
        puertas_data = self._dict.get('puertas', [])
        for puerta in puertas_data:
            # puerta = [num1, or1, num2, or2]
            self._builder.fabricarPuertaLado1Or1Lado2Or2(
                puerta[0], puerta[1], puerta[2], puerta[3]
            )
    
    def fabricarLaberintoRecursivo(self, dic: dict, padre):
        """
        Crea elementos recursivamente según su tipo.
        dic: diccionario con 'tipo', 'num', 'hijos'
        padre: contenedor padre (None para elementos raíz)
        """
        tipo = dic.get('tipo', '')
        contenedor = None
        
        # Crear según tipo
        if tipo == 'habitacion':
            contenedor = self._builder.fabricarHabitacion(dic.get('num', 0))
        
        elif tipo == 'armario':
            if padre:
                contenedor = self._builder.fabricarArmario(dic.get('num', 0), padre)
        
        elif tipo == 'bomba':
            if padre:
                self._builder.fabricarBombaEn(padre)
            return  # Las bombas no tienen hijos
        
        # Procesar hijos recursivamente
        hijos = dic.get('hijos', [])
        for hijo in hijos:
            self.fabricarLaberintoRecursivo(hijo, contenedor)
    
    # ==================== FABRICACIÓN DEL JUEGO ====================
    
    def fabricarJuego(self):
        """Crea el juego y le asigna el laberinto construido"""
        self._juego = Juego()
        self._juego.laberinto = self._builder.obtenerLaberinto()
        
        # Conectar el builder con el juego para que pueda usarlo
        self._builder.juego = self._juego
    
    # ==================== FABRICACIÓN DE BICHOS ====================
    
    def fabricarBichos(self):
        """Crea los bichos según los datos del JSON"""
        bichos_data = self._dict.get('bichos', [])
        
        if not bichos_data:
            return
        
        for bicho_data in bichos_data:
            modo = bicho_data.get('modo', 'Agresivo')
            posicion = bicho_data.get('posicion', 1)
            self._builder.fabricarBichoModo(modo, posicion)
    
    def __str__(self):
        return f"Director con builder={self._builder}"

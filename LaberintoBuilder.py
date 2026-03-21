from Builder import Builder
from Laberinto import Laberinto
from Habitacion import Habitacion
from Pared import Pared
from Puerta import Puerta
from Bomba import Bomba
from Armario import Armario
from Bicho import Bicho
from Agresivo import Agresivo
from Perezoso import Perezoso
from Orientaciones import Norte, Sur, Este, Oeste


class LaberintoBuilder(Builder):
    """
    ConcreteBuilder: Implementa la interfaz del Builder para construir y ensamblar
    partes del laberinto. Define y guarda la representación que crea.
    """
    
    def __init__(self):
        self._laberinto = None
        self._juego = None  # Referencia al juego (se establece desde Director)
    
    @property
    def laberinto(self):
        return self._laberinto
    
    @property
    def juego(self):
        return self._juego
    
    @juego.setter
    def juego(self, value):
        self._juego = value
    
    # ==================== FABRICACIÓN DE ELEMENTOS ====================
    
    def fabricarLaberinto(self):
        """Crea el laberinto vacío"""
        self._laberinto = Laberinto()
        return self._laberinto
    
    def fabricarHabitacion(self, num: int):
        """
        Crea una habitación con el número dado.
        Le asigna orientaciones y pone paredes en cada lado.
        """
        hab = Habitacion(num)
        self.asignarOrientaciones(hab)
        
        # Poner pared en cada orientación
        for orientacion in hab.orientaciones:
            hab.poner_en(orientacion, self.fabricarPared())
        
        self._laberinto.agregar_Habitacion(hab)
        return hab
    
    def fabricarPared(self):
        """Crea una pared"""
        return Pared()
    
    def fabricarPuerta(self, lado1, lado2):
        """Crea una puerta entre dos habitaciones"""
        puerta = Puerta(lado1, lado2)
        return puerta
    
    def fabricarPuertaLado1Or1Lado2Or2(self, num1: int, or1: str, num2: int, or2: str):
        """
        Crea una puerta entre dos habitaciones especificando:
        - num1: número de habitación 1
        - or1: orientación en hab1 (ej: "Norte")
        - num2: número de habitación 2
        - or2: orientación en hab2 (ej: "Sur")
        """
        puerta = Puerta(None, None)
        
        lado1 = self._laberinto.obtener_habitaciones(num1)
        lado2 = self._laberinto.obtener_habitaciones(num2)
        
        puerta.lado1 = lado1
        puerta.lado2 = lado2
        
        # Obtener objetos de orientación usando reflection
        obj_or1 = self._fabricar_orientacion(or1)
        obj_or2 = self._fabricar_orientacion(or2)
        
        # Poner la puerta en las orientaciones correspondientes
        lado1.poner_en(obj_or1, puerta)
        lado2.poner_en(obj_or2, puerta)
        
        return puerta
    
    def _fabricar_orientacion(self, nombre: str):
        """
        Reflection: Convierte string a objeto Orientación.
        'Norte' -> Norte(), 'Sur' -> Sur(), etc.
        """
        nombre = nombre.capitalize()
        if nombre == "Norte":
            return self.fabricarNorte()
        elif nombre == "Sur":
            return self.fabricarSur()
        elif nombre == "Este":
            return self.fabricarEste()
        elif nombre == "Oeste":
            return self.fabricarOeste()
        else:
            raise ValueError(f"Orientación desconocida: {nombre}")
    
    def fabricarBombaEn(self, contenedor):
        """Crea una bomba en el contenedor dado"""
        bomba = Bomba(Pared())  # La bomba decora una pared
        contenedor.agregar_hijo(bomba)
        return bomba
    
    def fabricarArmario(self, num: int, contenedor):
        """
        Crea un armario dentro de un contenedor.
        El armario tiene orientaciones y una puerta que lo conecta al contenedor.
        """
        armario = Armario(num)
        self.asignarOrientaciones(armario)
        
        # Poner pared en cada orientación
        for orientacion in armario.orientaciones:
            armario.poner_en(orientacion, self.fabricarPared())
        
        # Crear puerta entre armario y contenedor
        puerta = Puerta(armario, contenedor)
        armario.poner_en(self.fabricarEste(), puerta)
        
        # Añadir armario como hijo del contenedor
        contenedor.agregar_hijo(armario)
        
        return armario
    
    def fabricarBichoModo(self, str_modo: str, posicion: int):
        """
        Crea un bicho con el modo indicado y lo coloca en la habitación.
        str_modo: 'Agresivo' o 'Perezoso'
        posicion: número de habitación donde colocar el bicho
        """
        # Reflection: obtener el modo según string
        modo = self._fabricar_modo(str_modo)
        
        # Obtener habitación
        hab = self._juego.obtenerHabitacion(posicion) if self._juego else \
              self._laberinto.obtener_habitaciones(posicion)
        
        # Crear bicho
        bicho = Bicho(f"Bicho-{str_modo}", modo)
        
        # Entrar en la habitación
        hab.entrar(bicho)
        
        # Añadir al juego si existe
        if self._juego:
            self._juego.agregarBicho(bicho)
        
        return bicho
    
    def _fabricar_modo(self, nombre: str):
        """
        Reflection: Convierte string a objeto Modo.
        'Agresivo' -> Agresivo(), 'Perezoso' -> Perezoso()
        """
        nombre = nombre.capitalize()
        if nombre == "Agresivo":
            return self.fabricarAgresivo()
        elif nombre == "Perezoso":
            return self.fabricarPerezoso()
        else:
            raise ValueError(f"Modo desconocido: {nombre}")
    
    # ==================== FABRICACIÓN DE ORIENTACIONES (Singleton) ====================
    
    def fabricarNorte(self):
        return Norte()
    
    def fabricarSur(self):
        return Sur()
    
    def fabricarEste(self):
        return Este()
    
    def fabricarOeste(self):
        return Oeste()
    
    # ==================== FABRICACIÓN DE MODOS ====================
    
    def fabricarAgresivo(self):
        return Agresivo()
    
    def fabricarPerezoso(self):
        return Perezoso()
    
    # ==================== ASIGNACIÓN DE ORIENTACIONES ====================
    
    def asignarOrientaciones(self, contenedor):
        """Asigna las 4 orientaciones a un contenedor"""
        contenedor.agregar_orientacion(self.fabricarNorte())
        contenedor.agregar_orientacion(self.fabricarEste())
        contenedor.agregar_orientacion(self.fabricarSur())
        contenedor.agregar_orientacion(self.fabricarOeste())
    
    # ==================== OBTENER RESULTADO ====================
    
    def obtenerLaberinto(self):
        """Devuelve el laberinto construido (GetResult del patrón)"""
        return self._laberinto
    
    def __str__(self):
        return "LaberintoBuilder"

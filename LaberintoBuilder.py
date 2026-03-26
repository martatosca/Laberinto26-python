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
    
    
    def __init__(self):
        self._laberinto = None
        self._juego = None
    
    @property
    def laberinto(self):
        return self._laberinto
    
    @property
    def juego(self):
        return self._juego
    
    @juego.setter
    def juego(self, value):
        self._juego = value
    
    
    def fabricarLaberinto(self):
        
        self._laberinto = Laberinto()
        return self._laberinto
    
    def fabricarHabitacion(self, num: int):
        
        hab = Habitacion(num)
        self.asignarOrientaciones(hab)
        
        for orientacion in hab.orientaciones:
            hab.poner_en(orientacion, self.fabricarPared())
        
        self._laberinto.agregar_Habitacion(hab)
        return hab
    
    def fabricarPared(self):
        
        return Pared()
    
    def fabricarPuerta(self, lado1, lado2):
        
        puerta = Puerta(lado1, lado2)
        return puerta
    
    def fabricarPuertaLado1Or1Lado2Or2(self, num1: int, or1: str, num2: int, or2: str):
        
        puerta = Puerta(None, None)
        
        lado1 = self._laberinto.obtener_habitaciones(num1)
        lado2 = self._laberinto.obtener_habitaciones(num2)
        
        puerta.lado1 = lado1
        puerta.lado2 = lado2
        
        obj_or1 = self._fabricar_orientacion(or1)
        obj_or2 = self._fabricar_orientacion(or2)
        
        lado1.poner_en(obj_or1, puerta)
        lado2.poner_en(obj_or2, puerta)
        
        return puerta
    
    def _fabricar_orientacion(self, nombre: str):
        
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
        
        bomba = Bomba(Pared())
        contenedor.agregar_hijo(bomba)
        return bomba
    
    def fabricarArmario(self, num: int, contenedor):
        
        armario = Armario(num)
        self.asignarOrientaciones(armario)
        
        for orientacion in armario.orientaciones:
            armario.poner_en(orientacion, self.fabricarPared())
        
        puerta = Puerta(armario, contenedor)
        armario.poner_en(self.fabricarEste(), puerta)
        
        contenedor.agregar_hijo(armario)
        
        return armario
    
    def fabricarBichoModo(self, str_modo: str, posicion: int):
        
        modo = self._fabricar_modo(str_modo)
        
        hab = self._juego.obtenerHabitacion(posicion) if self._juego else \
              self._laberinto.obtener_habitaciones(posicion)
        
        bicho = Bicho(f"Bicho-{str_modo}", modo)
        
        hab.entrar(bicho)
        
        if self._juego:
            self._juego.agregarBicho(bicho)
        
        return bicho
    
    def _fabricar_modo(self, nombre: str):
        
        nombre = nombre.capitalize()
        if nombre == "Agresivo":
            return self.fabricarAgresivo()
        elif nombre == "Perezoso":
            return self.fabricarPerezoso()
        else:
            raise ValueError(f"Modo desconocido: {nombre}")
    
    
    def fabricarNorte(self):
        return Norte()
    
    def fabricarSur(self):
        return Sur()
    
    def fabricarEste(self):
        return Este()
    
    def fabricarOeste(self):
        return Oeste()
    
    
    def fabricarAgresivo(self):
        return Agresivo()
    
    def fabricarPerezoso(self):
        return Perezoso()
    
    
    def asignarOrientaciones(self, contenedor):
        
        contenedor.agregar_orientacion(self.fabricarNorte())
        contenedor.agregar_orientacion(self.fabricarEste())
        contenedor.agregar_orientacion(self.fabricarSur())
        contenedor.agregar_orientacion(self.fabricarOeste())
    
    
    def obtenerLaberinto(self):
        
        return self._laberinto
    
    def __str__(self):
        return "LaberintoBuilder"

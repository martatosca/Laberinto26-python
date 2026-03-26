from Habitacion import Habitacion
from Pared import Pared
from Puerta import Puerta
from Laberinto import Laberinto
from LaberintoFactory import LaberintoFactory

class Juego:
    def __init__(self, factory: LaberintoFactory = None):
        super().__init__()
        self.laberinto=None
        self._contador_habitaciones = 0
        self.bichos = []
        self._factory = factory
        
    def setFactory(self, factory: LaberintoFactory):
        
        self._factory = factory
    
    def fabricarLab2HabAF(self):
        
        if self._factory is None:
            raise ValueError("No se ha establecido una factory. Use setFactory() primero.")
        
        hab1 = self.fabricarHabitacion()
        hab2 = self.fabricarHabitacion()
        
        puerta = self._factory.fabricarPuerta(hab1, hab2)
        
        hab1.sur = puerta
        hab1.norte = self._factory.fabricarPared()
        hab1.este = self._factory.fabricarPared()
        hab1.oeste = self._factory.fabricarPared()
        
        hab2.norte = puerta
        hab2.sur = self._factory.fabricarPared()
        hab2.este = self._factory.fabricarPared()
        hab2.oeste = self._factory.fabricarPared()
        
        self.laberinto = self.fabricarLaberinto()
        self.laberinto.agregar_Habitacion(hab1)
        self.laberinto.agregar_Habitacion(hab2)
        
        return self.laberinto
    
    def fabricarPared(self):
        return Pared()
    
    def fabricarPuerta(self, lado1=None, lado2=None):
        return Puerta(lado1, lado2)
    
    def fabricarHabitacion(self, id_habitacion=None):
        if id_habitacion is None:
            self._contador_habitaciones += 1
            id_habitacion = self._contador_habitaciones
        return Habitacion(id_habitacion)
    
    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarPuertaLado1Lado2(self, unaHab: Habitacion, otraHab: Habitacion):
        puerta= self.fabricarPuerta()
        puerta.lado1=unaHab
        puerta.lado2=otraHab
        return puerta
    
    def fabricarLab2HabFM(self):
        hab1=self.fabricarHabitacion()
        hab2=self.fabricarHabitacion()        
        puerta=self.fabricarPuertaLado1Lado2(hab1, hab2)    
        hab1.sur=puerta
        hab1.norte=self.fabricarPared()
        hab1.este=self.fabricarPared()
        hab1.oeste=self.fabricarPared()
        hab2.norte=puerta
        hab2.sur=self.fabricarPared()
        hab2.este=self.fabricarPared()
        hab2.oeste=self.fabricarPared()
        
        self.laberinto=self.fabricarLaberinto()
        self.laberinto.agregar_Habitacion(hab1)
        self.laberinto.agregar_Habitacion(hab2)
        
        return self.laberinto
    
    def agregarBicho(self, bicho):
        
        self.bichos.append(bicho)
    
    def eliminarBicho(self, bicho):
        
        if bicho in self.bichos:
            self.bichos.remove(bicho)
    
    def obtenerBichos(self):
        
        return list(self.bichos)
    
    def obtenerHabitacion(self, num: int):
        
        return self.laberinto.obtener_habitaciones(num) if self.laberinto else None

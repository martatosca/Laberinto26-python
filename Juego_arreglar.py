from Habitacion import Habitacion
from Pared import Pared
from Puerta import Puerta
from Laberinto import Laberinto

#Juego es el creator de Factory Method
class Juego:
    def __init__(self):
        super().__init__()
        self.laberinto=None
        self._contador_habitaciones = 0  # Contador para generar IDs únicos
        self.bichos = []  # Lista de bichos del juego (0..*)
        
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
        #habitacion 1
        hab1.sur=puerta
        hab1.norte=self.fabricarPared()
        hab1.este=self.fabricarPared()
        hab1.oeste=self.fabricarPared()
        #habitacion 2
        hab2.norte=puerta
        hab2.sur=self.fabricarPared()
        hab2.este=self.fabricarPared()
        hab2.oeste=self.fabricarPared()
        
        self.laberinto=self.fabricarLaberinto()
        self.laberinto.agregar_Habitacion(hab1)
        self.laberinto.agregar_Habitacion(hab2)
        
        return self.laberinto
    
    def agregarBicho(self, bicho):
        """Añade un bicho al juego"""
        self.bichos.append(bicho)
    
    def eliminarBicho(self, bicho):
        """Elimina un bicho del juego"""
        if bicho in self.bichos:
            self.bichos.remove(bicho)
    
    def obtenerBichos(self):
        """Devuelve la lista de bichos"""
        return list(self.bichos)
    
    #product= ElementoMapa
    #concreteProduct= Habitacion, Pared, Puerta
    #creator= Juego
    #factoryMethod= fabricarPared, fabricarPuerta, fabricarHabitacion, fabricarLaberinto, fabricarPuertaLado1Lado2
    #anOperation(): fabricarLab2HabFM             
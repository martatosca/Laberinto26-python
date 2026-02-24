from Habitacion import Habitacion
from Pared import Pared
from Puerta import Puerta
from Laberinto import Laberinto

#Juego es el creator de Factory Method
class Juego:
    def __init__(self):
        super().__init__()
        self.laberinto=None
        
    def fabricarPared(self):
        return Pared()
    
    def fabricarPuerta(self):
        return Puerta()
    
    def fabricarHabitacion(self):
        return Habitacion()
    
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
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        
        return self.laberinto
    
    #product= ElementoMapa
    #concreteProduct= Habitacion, Pared, Puerta
    #creator= Juego
    #factoryMethod= fabricarPared, fabricarPuerta, fabricarHabitacion, fabricarLaberinto, fabricarPuertaLado1Lado2
    #anOperation(): fabricarLab2HabFM             
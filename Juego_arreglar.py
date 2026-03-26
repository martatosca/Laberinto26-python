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
        self.personaje = None
        self._factory = factory
    
    def notificar(self, emisor, evento: str, datos=None):
        if evento == "atacar":
            self._gestionar_ataque(emisor, datos)
        elif evento == "entrar_habitacion":
            self._gestionar_entrada_habitacion(emisor, datos)
        elif evento == "derrotado":
            self._gestionar_derrotado(emisor)
    
    def _gestionar_ataque(self, atacante, objetivo):
        if objetivo and hasattr(objetivo, 'recibir_dano'):
            dano = atacante.poder
            print(f"[Juego] {atacante.nombre} ataca a {objetivo.nombre} con {dano} de daño")
            objetivo.recibir_dano(dano)
    
    def _gestionar_entrada_habitacion(self, ente, habitacion):
        from Bicho import Bicho
        from Personaje import Personaje
        
        if isinstance(ente, Personaje):
            for bicho in self.bichos:
                if bicho.posicion == habitacion and bicho.esta_vivo():
                    print(f"[Juego] ¡{ente.nombre} se encuentra con {bicho.nombre}!")
        elif isinstance(ente, Bicho):
            if self.personaje and self.personaje.posicion == habitacion:
                print(f"[Juego] ¡{ente.nombre} se encuentra con {self.personaje.nombre}!")
    
    def _gestionar_derrotado(self, ente):
        from Bicho import Bicho
        if isinstance(ente, Bicho):
            self.eliminarBicho(ente)
            print(f"[Juego] {ente.nombre} ha sido eliminado del juego")
        
    def setFactory(self, factory: LaberintoFactory):
        
        self._factory = factory
    
    def fabricarLab2HabAF(self):
        
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
        bicho.juego = self
        self.bichos.append(bicho)
    
    def agregarPersonaje(self, personaje):
        personaje.juego = self
        self.personaje = personaje
    
    def eliminarBicho(self, bicho):
        
        if bicho in self.bichos:
            self.bichos.remove(bicho)
            bicho.juego = None
    
    def obtenerBichos(self):
        
        return list(self.bichos)
    
    def obtenerHabitacion(self, num: int):
        
        return self.laberinto.obtener_habitaciones(num) if self.laberinto else None

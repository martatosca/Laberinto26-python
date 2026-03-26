from Contenedor import Contenedor
from Cuadrado import Cuadrado
import random

class HabitacionCuadrada(Contenedor):
    
    
    def __init__(self, num: int):
        super().__init__(forma=Cuadrado())
        self.num = num
        self.id = num
        
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        
        self.orientaciones = self._forma.obtener_orientaciones()
    
    def reemplazar_lado(self, attr_name, nuevo):
        
        anterior = getattr(self, attr_name, None)
        if anterior is nuevo:
            return
        if anterior is not None:
            try:
                self.eliminar_hijo(anterior)
            except ValueError:
                pass
        setattr(self, attr_name, nuevo)
        if nuevo is not None and nuevo not in self.hijos:
            self.agregar_hijo(nuevo)
    
    def poner_en(self, orientacion, elemento):
        
        nombre = orientacion.obtener_nombre().lower()
        self.reemplazar_lado(nombre, elemento)
    
    def obtener_en(self, orientacion):
        
        nombre = orientacion.obtener_nombre().lower()
        return getattr(self, nombre, None)
    
    def obtener_orientacion_aleatoria(self):
        
        if self.orientaciones:
            return random.choice(self.orientaciones)
        return None
    
    def entrar(self, alguien=None):
        
        if alguien:
            print(f"{alguien} está en Hab-{self.num}")
            alguien.posicion = self
        else:
            print(f"Has entrado a la habitación cuadrada {self.num}")
    
    def __str__(self):
        return f"HabitacionCuadrada({self.num}) [N={self.norte}, S={self.sur}, E={self.este}, O={self.oeste}]"

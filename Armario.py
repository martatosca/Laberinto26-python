from Hoja import Hoja

class Armario(Hoja):
    
    
    def __init__(self, num: int = 0):
        super().__init__()
        self.num = num
        self.orientaciones = []
        self._elementos = {}
    
    def agregar_orientacion(self, orientacion):
        
        if orientacion not in self.orientaciones:
            self.orientaciones.append(orientacion)
    
    def poner_en(self, orientacion, elemento):
        
        self._elementos[orientacion] = elemento
        if hasattr(elemento, 'padre'):
            elemento.padre = self
    
    def obtener_en(self, orientacion):
        
        return self._elementos.get(orientacion, None)
    
    def obtener_orientacion_aleatoria(self):
        
        import random
        if self.orientaciones:
            return random.choice(self.orientaciones)
        return None
    
    def entrar(self, alguien=None):
        if alguien:
            print(f"{alguien} está en {self}")
            alguien.posicion = self
        else:
            print(f"Has entrado al armario {self.num}")
    
    def __str__(self):
        return f"Armario-{self.num}"

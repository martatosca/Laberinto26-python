from Hoja import Hoja

class Armario(Hoja):
    """
    Armario: Es un contenedor especial que puede estar dentro de una habitación.
    Hereda de Hoja pero tiene orientaciones como un Contenedor.
    Según el código del profesor, tiene num y orientaciones.
    """
    
    def __init__(self, num: int = 0):
        super().__init__()
        self.num = num
        self.orientaciones = []  # Lista de orientaciones (N, S, E, O)
        self._elementos = {}     # Diccionario: orientacion -> elemento
    
    def agregar_orientacion(self, orientacion):
        """Añade una orientación al armario"""
        if orientacion not in self.orientaciones:
            self.orientaciones.append(orientacion)
    
    def poner_en(self, orientacion, elemento):
        """Pone un elemento (pared, puerta) en una orientación"""
        self._elementos[orientacion] = elemento
        if hasattr(elemento, 'padre'):
            elemento.padre = self
    
    def obtener_en(self, orientacion):
        """Obtiene el elemento en una orientación"""
        return self._elementos.get(orientacion, None)
    
    def obtener_orientacion_aleatoria(self):
        """Devuelve una orientación al azar"""
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

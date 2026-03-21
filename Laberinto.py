from Contenedor import Contenedor

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()
        self.habitaciones = {}
    
    def agregar_Habitacion(self, habitacion):
        self.habitaciones[habitacion.id] = habitacion
        self.agregar_hijo(habitacion)
        
    def obtener_habitaciones(self,numero): #devuelve la habitacion con ese numero o None si no existe
        return self.habitaciones.get(numero, None)
    
    def obtener_primera_habitacion(self):
        """Obtiene la primera habitación del laberinto (la de menor número)"""
        if self.habitaciones:
            min_key = min(self.habitaciones.keys())
            return self.habitaciones[min_key]
        return None
    
    def entrar(self):
        print("Has entrado al laberinto")
    
    def __str__(self):
        return f"Laberinto con {len(self.habitaciones)} habitaciones"
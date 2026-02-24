from ElementoMapa import ElementoMapa

class Laberinto(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.habitaciones = []
    
    def agregarHabitacion(self, unaHab):
        self.habitaciones.append(unaHab)
    @property
    def habitaciones(self):
        return self._habitaciones
    
from Contenedor import Contenedor
from Cuadrado import Cuadrado
import random

class Habitacion(Contenedor):
    
    
    def __init__(self, id_habitacion):
        super().__init__(forma=Cuadrado())
        self.id = id_habitacion
        self.num = id_habitacion

        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        
        self.orientaciones = self._forma.obtener_orientaciones() if self._forma else []
        
    
    def reemplazar_lado(self, attr_name, nuevo):
        anterior = getattr(self, attr_name)
        if anterior is nuevo:
            return
        if anterior is not None:
            try:
                self.eliminar_hijo(anterior)
            except ValueError:
                pass
        setattr(self, attr_name, nuevo)
        if nuevo is not None:
            if nuevo not in self.hijos:
                self.agregar_hijo(nuevo)

    def setNorte(self, elemento):
        self.norte = elemento
        self.agregar_hijo(elemento)

    def setSur(self, elemento):
        self.sur = elemento
        self.agregar_hijo(elemento)

    def setEste(self, elemento):
        self.este = elemento
        self.agregar_hijo(elemento)

    def setOeste(self, elemento):
        self.oeste = elemento
        self.agregar_hijo(elemento)

    
    def agregar_orientacion(self, orientacion):
        
        if orientacion not in self.orientaciones:
            self.orientaciones.append(orientacion)
    
    def poner_en(self, orientacion, elemento):
        
        nombre = orientacion.obtener_nombre().lower()
        if nombre == "norte":
            self.reemplazar_lado("norte", elemento)
        elif nombre == "sur":
            self.reemplazar_lado("sur", elemento)
        elif nombre == "este":
            self.reemplazar_lado("este", elemento)
        elif nombre == "oeste":
            self.reemplazar_lado("oeste", elemento)
    
    def obtener_en(self, orientacion):
        
        nombre = orientacion.obtener_nombre().lower()
        if nombre == "norte":
            return self.norte
        elif nombre == "sur":
            return self.sur
        elif nombre == "este":
            return self.este
        elif nombre == "oeste":
            return self.oeste
        return None
    
    def obtener_orientacion_aleatoria(self):
        
        if self.orientaciones:
            return random.choice(self.orientaciones)
        return None

    def entrar(self, alguien=None):
        
        if alguien:
            print(f"{alguien} está en Hab-{self.id}")
            alguien.posicion = self
        else:
            print("Has entrado a la habitación:", self.id)

    def __str__(self):
        n = str(self.norte) if self.norte is not None else "None"
        s = str(self.sur) if self.sur is not None else "None"
        e = str(self.este) if self.este is not None else "None"
        o = str(self.oeste) if self.oeste is not None else "None"
        return f"Habitacion({self.id}) [N={n}, S={s}, E={e}, O={o}]"

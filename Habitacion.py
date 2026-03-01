from Contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self, id_habitacion):
        super().__init__()
        self.id = id_habitacion

        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

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

    def entrar(self):
        print("Has entrado a la habitación:", self.id)

    def __str__(self):
        n = str(self.norte) if self.norte is not None else "None"
        s = str(self.sur) if self.sur is not None else "None"
        e = str(self.este) if self.este is not None else "None"
        o = str(self.oeste) if self.oeste is not None else "None"
        return f"Habitacion({self.id}) [N={n}, S={s}, E={e}, O={o}]"
        
    
        
        
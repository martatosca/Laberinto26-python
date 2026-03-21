from Contenedor import Contenedor
import random

class Habitacion(Contenedor):
    def __init__(self, id_habitacion):
        super().__init__()
        self.id = id_habitacion
        self.num = id_habitacion  # Alias para compatibilidad con código del profesor

        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        
        self.orientaciones = []  # Lista de orientaciones (objetos Norte, Sur, Este, Oeste)
        
    """De esta forma evitamos duplicados: En Habitacion se sincronizan los 
    atributos norte/sur/este/oeste con la lista hijos del Composite para que el recorrido del Iterator sea coherente y no aparezcan elementos duplicados al reemplazar un lado."""
    def reemplazar_lado(self, attr_name, nuevo):
        anterior = getattr(self, attr_name)
        # Si estamos poniendo el mismo objeto, no hacemos nada
        if anterior is nuevo:
            return
        # Si había un elemento anterior en ese lado, lo quitamos del composite
        if anterior is not None:
            try:
                self.eliminar_hijo(anterior)
            except ValueError:
                # por si no estaba en la lista por cualquier motivo
                pass
        # Asignamos el nuevo
        setattr(self, attr_name, nuevo)
        # Si el nuevo no es None, lo añadimos como hijo si no estaba ya
        if nuevo is not None:
            if nuevo not in self.hijos:   # self.hijos existe en Contenedor
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

    # ==================== MÉTODOS PARA BUILDER ====================
    
    def agregar_orientacion(self, orientacion):
        """Añade una orientación a la lista de orientaciones"""
        if orientacion not in self.orientaciones:
            self.orientaciones.append(orientacion)
    
    def poner_en(self, orientacion, elemento):
        """
        Pone un elemento (pared, puerta) en una orientación dada.
        Método genérico que usa el nombre de la orientación.
        """
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
        """Obtiene el elemento en una orientación dada"""
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
        """Devuelve una orientación al azar de las disponibles"""
        if self.orientaciones:
            return random.choice(self.orientaciones)
        return None

    def entrar(self, alguien=None):
        """Entra en la habitación. Si se pasa alguien, actualiza su posición."""
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
        
    
        
        
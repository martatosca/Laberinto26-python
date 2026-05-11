# LaberintoBuilder: Builder concreto para laberintos cuadrados (4 lados)
from Juego import Juego
from Laberinto import Laberinto
from Habitacion import Habitacion
from Cuadrado import Cuadrado
from Pared import Pared
from Puerta import Puerta
from Bomba import Bomba
from Armario import Armario
from Bicho import Bicho
from Agresivo import Agresivo
from Perezoso import Perezoso
from Orientaciones import Norte, Sur, Este, Oeste, Noreste, Noroeste, Sureste, Suroeste
from Abrir import Abrir
from Tunel import Tunel


class LaberintoBuilder:
    """Builder concreto que construye laberintos con habitaciones cuadradas."""

    def __init__(self):
        self._laberinto = None
        self._juego = None

    # ------------------------------------------------------------------
    # Getters
    # ------------------------------------------------------------------

    @property
    def laberinto(self):
        return self._laberinto

    @property
    def juego(self):
        return self._juego

    @juego.setter
    def juego(self, value):
        self._juego = value

    def obtener_laberinto(self):
        return self._laberinto

    # ------------------------------------------------------------------
    # Fabricacion de elementos basicos
    # ------------------------------------------------------------------

    def fabricar_laberinto(self):
        self._laberinto = Laberinto()
        return self._laberinto

    def fabricar_pared(self):
        return Pared()

    def fabricar_puerta(self):
        return Puerta()

    def fabricar_forma(self):
        forma = Cuadrado()
        self._asignar_orientaciones(forma)
        return forma

    def fabricar_norte(self):    return Norte()
    def fabricar_sur(self):     return Sur()
    def fabricar_este(self):    return Este()
    def fabricar_oeste(self):   return Oeste()
    def fabricar_noreste(self): return Noreste()
    def fabricar_noroeste(self): return Noroeste()
    def fabricar_sureste(self): return Sureste()
    def fabricar_suroeste(self): return Suroeste()

    def fabricar_agresivo(self): return Agresivo()
    def fabricar_perezoso(self): return Perezoso()

    # ------------------------------------------------------------------
    # Metodos del Builder
    # ------------------------------------------------------------------

    def fabricar_habitacion(self, num: int):
        """Crea una habitacion, la rodea de paredes y la agrega al laberinto."""
        hab = Habitacion(num)
        hab.forma = self.fabricar_forma()
        for or_ in hab.forma.orientaciones:
            hab.poner_en(or_, self.fabricar_pared())
        self._laberinto.agregar_habitacion(hab)
        return hab

    def fabricar_puerta_lado1_or1_lado2_or2(self, num1, or1, num2, or2):
        """Crea una puerta entre dos habitaciones según sus orientaciones."""
        pt = self.fabricar_puerta()
        lado1 = self._laberinto.obtener_habitacion(num1)
        lado2 = self._laberinto.obtener_habitacion(num2)
        pt.lado1 = lado1
        pt.lado2 = lado2
        obj_or1 = self._map_orientacion(or1)
        obj_or2 = self._map_orientacion(or2)
        lado1.poner_en(obj_or1, pt)
        lado2.poner_en(obj_or2, pt)
        # Asociar comando Abrir a la puerta
        cmd = Abrir()
        cmd.receptor = pt
        pt.agregar_comando(cmd)
        return pt

    def fabricar_bomba_en(self, contenedor):
        """Crea una bomba y la agrega como hijo del contenedor."""
        bomba = Bomba()
        contenedor.agregar_hijo(bomba)
        return bomba

    def fabricar_armario(self, num: int, contenedor):
        """Crea un armario, lo rodea de paredes, anade una puerta al contenedor."""
        armario = Armario(num)
        armario.forma = self.fabricar_forma()
        for or_ in armario.forma.orientaciones:
            armario.poner_en(or_, self.fabricar_pared())
        pt = self.fabricar_puerta()
        pt.lado1 = armario
        pt.lado2 = contenedor
        armario.poner_en(self.fabricar_este(), pt)
        contenedor.agregar_hijo(armario)
        return armario

    def fabricar_bicho_modo(self, str_modo: str, posicion: int):
        """Crea un bicho con el modo dado y lo coloca en la habitacion indicada."""
        modo = self._map_modo(str_modo)
        hab = self._juego.obtener_habitacion(posicion)
        bicho = Bicho()
        bicho.modo = modo
        hab.entrar(bicho)
        self._juego.agregar_bicho(bicho)
        bicho.juego = self._juego
        return bicho

    def fabricar_tunel_en(self, contenedor):
        """Crea un tunel y lo agrega como hijo del contenedor."""
        tunel = Tunel()
        contenedor.agregar_hijo(tunel)
        return tunel

    def fabricar_juego(self):
        """Crea el Juego, guarda el laberinto como prototipo y usa un clon."""
        self._juego = Juego()
        self._juego.prototipo = self._laberinto
        self._juego.laberinto = self._juego.clonar()
        return self._juego

    # ------------------------------------------------------------------
    # Helpers internos
    # ------------------------------------------------------------------

    def _asignar_orientaciones(self, forma):
        """Agrega las 4 orientaciones cardinales a la forma."""
        forma.agregar_orientacion(self.fabricar_norte())
        forma.agregar_orientacion(self.fabricar_este())
        forma.agregar_orientacion(self.fabricar_sur())
        forma.agregar_orientacion(self.fabricar_oeste())

    def _map_orientacion(self, nombre: str):
        nombre = str(nombre).capitalize()
        mapping = {
            'Norte': self.fabricar_norte,
            'Sur':   self.fabricar_sur,
            'Este':  self.fabricar_este,
            'Oeste': self.fabricar_oeste,
        }
        if nombre not in mapping:
            raise ValueError(f"Orientacion desconocida: {nombre}")
        return mapping[nombre]()

    def _map_modo(self, nombre: str):
        nombre = str(nombre).capitalize()
        if nombre == 'Agresivo':
            return self.fabricar_agresivo()
        elif nombre == 'Perezoso':
            return self.fabricar_perezoso()
        raise ValueError(f"Modo desconocido: {nombre}")

    def __str__(self):
        return "LaberintoBuilder"

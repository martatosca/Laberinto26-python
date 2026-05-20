# Juego: clase principal del juego del laberinto
# Actualizado con condiciones de fin de juego
import threading
import copy

from Laberinto import Laberinto
from Habitacion import Habitacion
from Pared import Pared
from Puerta import Puerta
from Personaje import Personaje
from Orientaciones import Norte, Sur, Este, Oeste


class Juego:
    """Juego es la clase principal del juego del laberinto."""

    def __init__(self):
        self.laberinto = None
        self.bichos = []
        self.person = None
        self.hilos = {}
        self.prototipo = None
        self.terminado = False    # NUEVO: flag de fin de juego

    # -----------------------------------------------------------------------
    # Acciones sobre el laberinto
    # -----------------------------------------------------------------------

    def abrir_puertas(self):
        self.laberinto.recorrer(
            lambda each: each.abrir() if each.es_puerta() else None)

    def cerrar_puertas(self):
        self.laberinto.recorrer(
            lambda each: each.cerrar() if each.es_puerta() else None)

    def activar_bombas(self):
        self.laberinto.recorrer(
            lambda each: each.activar() if each.es_bomba() else None)

    def desactivar_bombas(self):
        self.laberinto.recorrer(
            lambda each: each.desactivar() if each.es_bomba() else None)

    # -----------------------------------------------------------------------
    # Gestion del personaje
    # -----------------------------------------------------------------------

    def agregar_personaje(self, nombre):
        self.person = Personaje()
        self.person.nombre = nombre
        self.person.juego = self
        hab1 = self.obtener_habitacion(1)
        hab1.entrar(self.person)

    # -----------------------------------------------------------------------
    # Gestion de bichos
    # -----------------------------------------------------------------------

    def agregar_bicho(self, bicho):
        self.bichos.append(bicho)

    def eliminar_bicho(self, bicho):
        if bicho in self.bichos:
            self.bichos.remove(bicho)

    def lanzar_bicho(self, bicho):
        print(f"{bicho} se activa")

        def _run():
            while bicho.esta_vivo() and not self.terminado:
                bicho.actua()

        proceso = threading.Thread(target=_run, daemon=True)
        self.hilos[bicho] = proceso
        proceso.start()

    def lanzar_todos_los_bichos(self):
        print("Los bichos despiertan...")
        for bicho in self.bichos:
            self.lanzar_bicho(bicho)

    def terminar_bicho(self, bicho):
        bicho.vidas = 0
        print(f"{bicho} muere")

    def terminar_todos_los_bichos(self):
        for bicho in self.bichos:
            self.terminar_bicho(bicho)

    # -----------------------------------------------------------------------
    # Ataques
    # -----------------------------------------------------------------------

    def buscar_bicho(self):
        for bicho in self.bichos:
            if bicho.esta_vivo() and bicho.posicion == self.person.posicion:
                return bicho
        return None

    def buscar_personaje(self, bicho):
        if bicho.posicion == self.person.posicion:
            return self.person
        return None

    def muere_bicho(self, bicho):
        self.terminar_bicho(bicho)
        if self.todos_muertos():
            print(f"\n¡Todos los bichos han muerto! Pero aún necesitas encontrar la salida...")

    def muere_personaje(self):
        """CONDICION DE DERROTA: el personaje pierde todas sus vidas."""
        if self.terminado:
            return
        self.terminado = True
        print("\n" + "="*50)
        print("  ¡Has sido derrotado! Fin del juego.")
        print("  El personaje ha perdido todas sus vidas.")
        print("="*50 + "\n")
        self.terminar_todos_los_bichos()

    def gana_personaje(self):
        """CONDICION DE VICTORIA: el personaje llega a la salida con la llave."""
        if self.terminado:
            return
        self.terminado = True
        print("\n" + "="*50)
        print(f"  ¡¡¡{self.person} ha GANADO el juego!!!")
        print("  Has encontrado la llave y escapado del laberinto.")
        print("="*50 + "\n")
        self.terminar_todos_los_bichos()

    def todos_muertos(self):
        return not any(b.esta_vivo() for b in self.bichos)

    def esta_terminado(self):
        return self.terminado

    # -----------------------------------------------------------------------
    # Prototipo
    # -----------------------------------------------------------------------

    def clonar(self):
        return copy.deepcopy(self.prototipo)

    # -----------------------------------------------------------------------
    # Acceso al laberinto
    # -----------------------------------------------------------------------

    def numero_habitaciones(self):
        return self.laberinto.numero_habitaciones()

    def obtener_habitacion(self, num):
        return self.laberinto.obtener_habitacion(num)

    # -----------------------------------------------------------------------
    # Factory Methods
    # -----------------------------------------------------------------------

    def fabricar_norte(self):   return Norte()
    def fabricar_sur(self):     return Sur()
    def fabricar_este(self):    return Este()
    def fabricar_oeste(self):   return Oeste()

    def fabricar_pared(self):
        return Pared()

    def fabricar_puerta(self):
        return Puerta()

    def fabricar_habitacion(self, num):
        from Cuadrado import Cuadrado
        hab = Habitacion(num)
        hab.forma = Cuadrado()
        hab.forma.num = num
        self._asignar_orientaciones(hab)
        for or_ in hab.forma.orientaciones:
            hab.poner_en(or_, self.fabricar_pared())
        return hab

    def fabricar_laberinto(self):
        return Laberinto()

    def fabricar_puerta_lado1_lado2(self, hab1, hab2):
        pt = self.fabricar_puerta()
        pt.lado1 = hab1
        pt.lado2 = hab2
        return pt

    def _asignar_orientaciones(self, contenedor):
        contenedor.agregar_orientacion(self.fabricar_norte())
        contenedor.agregar_orientacion(self.fabricar_este())
        contenedor.agregar_orientacion(self.fabricar_sur())
        contenedor.agregar_orientacion(self.fabricar_oeste())

    # -----------------------------------------------------------------------
    # Construccion de laberintos
    # -----------------------------------------------------------------------

    def fabricar_lab2hab_fm(self):
        hab1 = self.fabricar_habitacion(1)
        hab2 = self.fabricar_habitacion(2)
        puerta = self.fabricar_puerta_lado1_lado2(hab1, hab2)
        hab1.poner_en(self.fabricar_sur(), puerta)
        hab2.poner_en(self.fabricar_norte(), puerta)
        self.laberinto = self.fabricar_laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)

    def fabricar_lab4hab_fm(self):
        hab1 = self.fabricar_habitacion(1)
        hab2 = self.fabricar_habitacion(2)
        hab3 = self.fabricar_habitacion(3)
        hab4 = self.fabricar_habitacion(4)
        p12 = self.fabricar_puerta_lado1_lado2(hab1, hab2)
        p13 = self.fabricar_puerta_lado1_lado2(hab1, hab3)
        p24 = self.fabricar_puerta_lado1_lado2(hab2, hab4)
        p34 = self.fabricar_puerta_lado1_lado2(hab3, hab4)
        hab1.poner_en(self.fabricar_sur(),  p12)
        hab2.poner_en(self.fabricar_norte(), p12)
        hab1.poner_en(self.fabricar_este(),  p13)
        hab3.poner_en(self.fabricar_oeste(), p13)
        hab2.poner_en(self.fabricar_este(),  p24)
        hab4.poner_en(self.fabricar_oeste(), p24)
        hab3.poner_en(self.fabricar_sur(),  p34)
        hab4.poner_en(self.fabricar_norte(), p34)
        self.laberinto = self.fabricar_laberinto()
        for h in [hab1, hab2, hab3, hab4]:
            self.laberinto.agregar_habitacion(h)

    def fabricar_lab4hab2bm_fm(self):
        from Bomba import Bomba
        self.fabricar_lab4hab_fm()
        bm1 = Bomba()
        self.obtener_habitacion(1).agregar_hijo(bm1)
        bm2 = Bomba()
        self.obtener_habitacion(3).agregar_hijo(bm2)

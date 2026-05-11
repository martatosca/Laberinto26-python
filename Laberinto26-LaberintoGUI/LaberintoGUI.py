# LaberintoGUI: interfaz grafica del laberinto (equivalente a Pharo Morphic)
import sys
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder', 'Laberinto26-Visitor']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from Director import Director


class LaberintoGUI:
    """Interfaz grafica del laberinto.

    En Pharo hereda de BorderedMorph (Morphic).
    Aqui es un stub pendiente de implementar con tkinter o similar.
    """

    def __init__(self):
        self.juego = None
        self.person = None
        self.win = None

    def iniciar_juego(self):
        """Carga el laberinto desde JSON y lo muestra."""
        ruta = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'laberintos', 'lab4Hab4bm2bichosTunel.json')
        director = Director()
        director.procesar(ruta)
        self.juego = director.obtener_juego()
        self.mostrar_laberinto()

    def mostrar_laberinto(self):
        """Calcula la posicion y dibuja el laberinto (pendiente de implementar)."""
        self._calcular_posicion()

    def _calcular_posicion(self):
        """Calcula la posicion relativa de las habitaciones respecto de hab1."""
        pass  # pendiente de implementar

    def __str__(self):
        return "LaberintoGUI"

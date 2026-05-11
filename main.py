"""
Punto de entrada principal del laberinto.
Equivalente a un playground de Pharo que usa Director para construir el juego.
"""
import sys
import os

_ROOT = os.path.dirname(os.path.abspath(__file__))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder', 'Laberinto26-Visitor']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)

from Director import Director
from VisitorAbrirPuertas import VisitorAbrirPuertas
from VisitorCerrarPuertas import VisitorCerrarPuertas

_RUTA = os.path.join(_ROOT, 'laberintos', 'lab4Hab4bm2bichosTunel.json')


if __name__ == '__main__':
    director = Director()
    director.procesar(_RUTA)
    juego = director.obtener_juego()
    juego.agregar_personaje('Pepe')

    print("\n--- abrirPuertas ---")
    juego.abrir_puertas()

    print("\n--- cerrarPuertas (Visitor) ---")
    vcp = VisitorCerrarPuertas()
    juego.laberinto.aceptar(vcp)

    print("\n--- abrirPuertas (Visitor) ---")
    vap = VisitorAbrirPuertas()
    juego.laberinto.aceptar(vap)

    print("\n--- lanzarTodosLosBichos ---")
    juego.lanzar_todos_los_bichos()


"""Pruebas del LaberintoBuilder.
Traduccion fiel de LaberintoBuilderTest de Pharo.
"""
import sys
import os
import unittest

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder', 'Laberinto26-Visitor']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from Director import Director
from VisitorAbrirPuertas import VisitorAbrirPuertas
from VisitorCerrarPuertas import VisitorCerrarPuertas

_RUTA = os.path.join(_ROOT, 'laberintos', 'lab4Hab4bm2bichosTunel.json')


class LaberintoBuilderTest(unittest.TestCase):
    """Equivalente a LaberintoBuilderTest de Pharo."""

    def setUp(self):
        self.director = Director()
        self.director.procesar(_RUTA)
        self.dict = self.director.dict
        self.juego = self.director.obtener_juego()
        self.juego.agregar_personaje('Pepe')

    # ------------------------------------------------------------------
    # Helpers (comprobar*)
    # ------------------------------------------------------------------

    def comprobar_habitacion(self, num):
        hab = self.juego.obtener_habitacion(num)
        self.assertEqual(hab.num, num)
        return hab

    def comprobar_armario(self, num, contenedor):
        arm = next((h for h in contenedor.hijos if h.es_armario()), None)
        self.assertTrue(arm.es_armario())
        return arm

    def comprobar_bomba_en(self, contenedor):
        bmb = next((h for h in contenedor.hijos if h.es_bomba()), None)
        self.assertTrue(bmb.es_bomba())
        self._comprobar_funcionamiento_bomba(bmb)

    def _comprobar_funcionamiento_bomba(self, una_bomba):
        pass  # stub (igual que en Pharo)

    def comprobar_tunel_en(self, contenedor):
        tunel = next((h for h in contenedor.hijos if h.es_tunel()), None)
        self.assertTrue(tunel.es_tunel())
        self._comprobar_funcionamiento_tunel(tunel)

    def _comprobar_funcionamiento_tunel(self, un_tunel):
        self.assertTrue(un_tunel.es_tunel())
        self.assertIsNone(un_tunel.laberinto)
        self.assertIsNotNone(self.juego.person)
        un_tunel.entrar(self.juego.person)
        self.assertIsNotNone(un_tunel.laberinto)
        self.assertEqual(self.juego.numero_habitaciones(),
                         un_tunel.laberinto.numero_habitaciones())

    def comprobar_puerta_de(self, num1, or1, num2, or2):
        una_hab = self.juego.obtener_habitacion(num1)
        otra_hab = self.juego.obtener_habitacion(num2)
        self.assertEqual(una_hab.num, num1)
        self.assertEqual(otra_hab.num, num2)
        obj_or1 = getattr(self.director.builder, f'fabricar_{or1.lower()}')()
        obj_or2 = getattr(self.director.builder, f'fabricar_{or2.lower()}')()
        pt1 = una_hab.obtener_elemento(obj_or1)
        pt2 = otra_hab.obtener_elemento(obj_or2)
        self.assertTrue(pt1.es_puerta())
        self.assertTrue(pt2.es_puerta())
        self.assertIs(pt1, pt2)
        self.assertFalse(pt1.esta_abierta())

    def comprobar_laberinto_recursivo(self, dic, padre):
        nada = True
        contenedor = None
        if dic.get('tipo') == 'habitacion':
            nada = False
            contenedor = self.comprobar_habitacion(dic.get('num'))
        if dic.get('tipo') == 'armario':
            nada = False
            contenedor = self.comprobar_armario(dic.get('num'), padre)
        if dic.get('tipo') == 'bomba':
            nada = False
            self.comprobar_bomba_en(padre)
        if dic.get('tipo') == 'tunel':
            nada = False
            self.comprobar_tunel_en(padre)
        lista = dic.get('hijos')
        if lista:
            for each in lista:
                self.comprobar_laberinto_recursivo(each, contenedor)
        if nada:
            self.fail("tipo desconocido en JSON")

    # ------------------------------------------------------------------
    # Tests
    # ------------------------------------------------------------------

    def test_iniciales(self):
        self.assertIsNotNone(self.juego)
        self.assertIsNotNone(self.juego.laberinto)
        self.assertIsNotNone(self.juego.person)

    def test_laberinto(self):
        for each in self.dict.get('laberinto', []):
            self.comprobar_laberinto_recursivo(each, 'root')
        for cada in self.dict.get('puertas', []):
            self.comprobar_puerta_de(cada[0], cada[1], cada[2], cada[3])

    def test_puertas(self):
        puertas = set()
        self.juego.laberinto.recorrer(
            lambda each: puertas.add(each) if each.es_puerta() else None)
        # Inicialmente todas cerradas
        self.assertFalse(any(p.esta_abierta() for p in puertas))
        # Abrir todas
        self.juego.abrir_puertas()
        self.assertFalse(any(p.esta_cerrada() for p in puertas))
        # Cerrar todas
        self.juego.cerrar_puertas()
        self.assertFalse(any(p.esta_abierta() for p in puertas))
        # Probar que una puerta cerrada no mueve al personaje
        una_puerta = next(iter(puertas))
        self.juego.person.posicion = una_puerta.lado1
        posicion = self.juego.person.posicion
        una_puerta.entrar(self.juego.person)
        self.assertEqual(posicion, self.juego.person.posicion)
        # Abrir y probar que si mueve
        self.juego.abrir_puertas()
        una_puerta.entrar(self.juego.person)
        self.assertNotEqual(posicion, self.juego.person.posicion)
        self.assertIs(self.juego.person.posicion, una_puerta.lado2)

    def test_puertas_abiertas_visitor(self):
        puertas = set()
        self.juego.laberinto.recorrer(
            lambda each: puertas.add(each) if each.es_puerta() else None)
        self.assertFalse(any(p.esta_abierta() for p in puertas))
        vAP = VisitorAbrirPuertas()
        self.juego.laberinto.aceptar(vAP)
        self.assertFalse(any(p.esta_cerrada() for p in puertas))
        vCP = VisitorCerrarPuertas()
        self.juego.laberinto.aceptar(vCP)
        self.assertFalse(any(p.esta_abierta() for p in puertas))

    def test_gana_personaje(self):
        self.juego.terminar_todos_los_bichos()
        self.assertTrue(self.juego.todos_muertos())

    def test_ganan_bichos(self):
        pass  # ToDo (igual que en Pharo)


if __name__ == '__main__':
    unittest.main()


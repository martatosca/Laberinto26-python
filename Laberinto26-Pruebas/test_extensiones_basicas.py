"""Pruebas de las 5 extensiones basicas del laberinto."""
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
from Trampa import Trampa
from Escalera import Escalera
from ParedTransparente import ParedTransparente
from Dormido import Dormido
from BichoFuerte import BichoFuerte
from Orientaciones import Sur

_RUTA = os.path.join(_ROOT, 'laberintos', 'lab_modificaciones.json')


class ExtensionesBasicasTest(unittest.TestCase):
    """Pruebas de las 5 extensiones basicas."""

    def setUp(self):
        self.director = Director()
        self.director.procesar(_RUTA)
        self.juego = self.director.obtener_juego()
        self.juego.agregar_personaje('Pepe')

    # ------------------------------------------------------------------
    # Extension 1: Trampa
    # ------------------------------------------------------------------

    def test_trampa_existe_en_habitacion1(self):
        """Hab1 debe contener una Trampa con danio=10."""
        hab1 = self.juego.obtener_habitacion(1)
        trampa = next((h for h in hab1.hijos if h.es_trampa()), None)
        self.assertIsNotNone(trampa, "No se encontro Trampa en hab1")
        self.assertIsInstance(trampa, Trampa)
        self.assertEqual(trampa.danio, 10)

    def test_trampa_reduce_vidas(self):
        """Entrar en la trampa debe reducir las vidas del ente."""
        hab1 = self.juego.obtener_habitacion(1)
        trampa = next((h for h in hab1.hijos if h.es_trampa()), None)
        self.assertIsNotNone(trampa)
        person = self.juego.person
        vidas_antes = person.vidas
        trampa.entrar(person)
        self.assertEqual(person.vidas, vidas_antes - trampa.danio)

    # ------------------------------------------------------------------
    # Extension 2: Escalera
    # ------------------------------------------------------------------

    def test_escalera_existe_en_habitacion2(self):
        """Hab2 debe contener una Escalera."""
        hab2 = self.juego.obtener_habitacion(2)
        escalera = next((h for h in hab2.hijos if h.es_escalera()), None)
        self.assertIsNotNone(escalera, "No se encontro Escalera en hab2")
        self.assertIsInstance(escalera, Escalera)

    def test_escalera_teleporta_a_habitacion4(self):
        """Entrar en la escalera de hab2 debe mover al ente a hab4."""
        hab2 = self.juego.obtener_habitacion(2)
        hab4 = self.juego.obtener_habitacion(4)
        escalera = next((h for h in hab2.hijos if h.es_escalera()), None)
        self.assertIsNotNone(escalera)
        person = self.juego.person
        escalera.entrar(person)
        self.assertIs(person.posicion, hab4)

    # ------------------------------------------------------------------
    # Extension 3: Bicho Dormido
    # ------------------------------------------------------------------

    def test_bicho_dormido_en_habitacion3(self):
        """El bicho de hab3 debe tener modo Dormido."""
        hab3 = self.juego.obtener_habitacion(3)
        bicho_dormido = next(
            (b for b in self.juego.bichos if b.posicion is hab3), None)
        self.assertIsNotNone(bicho_dormido, "No se encontro bicho en hab3")
        self.assertIsInstance(bicho_dormido.modo, Dormido)
        self.assertTrue(bicho_dormido.modo.es_dormido())

    def test_bicho_dormido_no_ataca(self):
        """El bicho dormido no causa dano al atacar (solo imprime mensaje)."""
        hab3 = self.juego.obtener_habitacion(3)
        bicho_dormido = next(
            (b for b in self.juego.bichos if b.posicion is hab3), None)
        self.assertIsNotNone(bicho_dormido)
        person = self.juego.person
        vidas_antes = person.vidas
        bicho_dormido.modo.ataca(bicho_dormido)
        self.assertEqual(person.vidas, vidas_antes)

    # ------------------------------------------------------------------
    # Extension 4: ParedTransparente
    # ------------------------------------------------------------------

    def test_pared_transparente_en_habitacion3_sur(self):
        """La pared Sur de hab3 debe ser ParedTransparente."""
        hab3 = self.juego.obtener_habitacion(3)
        pared_sur = hab3.obtener_elemento(Sur())
        self.assertIsInstance(pared_sur, ParedTransparente)
        self.assertTrue(pared_sur.es_pared_transparente())

    def test_pared_transparente_descripcion(self):
        """La ParedTransparente de hab3-Sur debe tener la descripcion correcta."""
        hab3 = self.juego.obtener_habitacion(3)
        pared_sur = hab3.obtener_elemento(Sur())
        self.assertIsInstance(pared_sur, ParedTransparente)
        self.assertIn("escalera", pared_sur.descripcion_otro_lado.lower())

    # ------------------------------------------------------------------
    # Extension 5: BichoFuerte
    # ------------------------------------------------------------------

    def test_bicho_fuerte_en_habitacion4(self):
        """El bicho de hab4 debe ser BichoFuerte con vidas=100 y poder=2."""
        hab4 = self.juego.obtener_habitacion(4)
        bicho_fuerte = next(
            (b for b in self.juego.bichos if b.posicion is hab4), None)
        self.assertIsNotNone(bicho_fuerte, "No se encontro bicho en hab4")
        self.assertIsInstance(bicho_fuerte, BichoFuerte)
        self.assertEqual(bicho_fuerte.vidas, 100)
        self.assertEqual(bicho_fuerte.poder, 2)


if __name__ == '__main__':
    unittest.main()

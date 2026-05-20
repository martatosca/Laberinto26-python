"""
Tests de las 2 extensiones medias:
  - TestLlave          (Media 1: Inventario + Llave)
  - TestEstadoBloqueada (Media 2: PuertaSalida + estado Bloqueada)
  - TestHabitacionSalida
  - TestCondicionesFinJuego
"""
import unittest
from unittest.mock import MagicMock, patch


# -----------------------------------------------------------------------
# Stubs
# -----------------------------------------------------------------------

class _Ente:
    def __init__(self, nombre="Jugador"):
        self.nombre = nombre
        self.vidas = 50
        self.poder = 1
        self.posicion = None
        self.juego = MagicMock()
        self.inventario = []
        self._murio = False

    def muero(self):
        self._murio = True
        self.juego.muere_personaje()

    def es_llave(self):
        return False

    def __str__(self):
        return self.nombre


# -----------------------------------------------------------------------
# TestLlave
# -----------------------------------------------------------------------

class TestLlave(unittest.TestCase):
    """Tests para la extension Media 1: Llave."""

    def setUp(self):
        from Llave import Llave
        self.Llave = Llave

    def test_llave_se_anade_al_inventario(self):
        """Al entrar en una llave, esta se anade al inventario del personaje."""
        llave = self.Llave()
        ente = _Ente()
        llave.entrar(ente)
        self.assertIn(llave, ente.inventario)

    def test_llave_queda_recogida(self):
        """Tras recogerla, llave.recogida es True."""
        llave = self.Llave()
        ente = _Ente()
        llave.entrar(ente)
        self.assertTrue(llave.recogida)

    def test_llave_no_se_recoge_dos_veces(self):
        """Una llave ya recogida no se anade dos veces al inventario."""
        llave = self.Llave()
        ente = _Ente()
        llave.entrar(ente)
        llave.entrar(ente)
        self.assertEqual(len(ente.inventario), 1)

    def test_llave_es_llave(self):
        llave = self.Llave()
        self.assertTrue(llave.es_llave())

    def test_llave_no_es_puerta(self):
        llave = self.Llave()
        self.assertFalse(llave.es_puerta())

    def test_ente_sin_inventario_no_falla(self):
        """Si el ente no tiene inventario, entrar() no lanza excepcion."""
        llave = self.Llave()
        ente = MagicMock()
        del ente.inventario   # eliminar atributo para simular ente sin inventario
        ente.__str__ = lambda s: "Bicho"
        try:
            llave.entrar(ente)
        except Exception as e:
            self.fail(f"entrar() lanzo excepcion inesperada: {e}")

    def test_llave_str(self):
        llave = self.Llave()
        self.assertIn("Llave", str(llave))


# -----------------------------------------------------------------------
# TestPersonajeInventario
# -----------------------------------------------------------------------

class TestPersonajeInventario(unittest.TestCase):
    """Tests para el inventario del Personaje (parte de Media 1)."""

    def setUp(self):
        from Personaje import Personaje
        self.Personaje = Personaje

    def test_personaje_tiene_inventario(self):
        p = self.Personaje()
        self.assertIsInstance(p.inventario, list)

    def test_personaje_inventario_vacio_al_inicio(self):
        p = self.Personaje()
        self.assertEqual(len(p.inventario), 0)

    def test_personaje_tiene_llave_false_sin_llave(self):
        p = self.Personaje()
        self.assertFalse(p.tiene_llave())

    def test_personaje_tiene_llave_true_con_llave(self):
        from Llave import Llave
        p = self.Personaje()
        llave = Llave()
        llave.recogida = True
        p.inventario.append(llave)
        self.assertTrue(p.tiene_llave())

    def test_personaje_coger_llave_en_habitacion(self):
        """coger_llave() recoge la llave de la habitacion actual."""
        from Llave import Llave
        p = self.Personaje()
        p.nombre = "Jugador"
        p.juego = MagicMock()

        hab = MagicMock()
        llave = Llave()
        hab.hijos = [llave]
        p.posicion = hab

        p.coger_llave()
        self.assertIn(llave, p.inventario)

    def test_personaje_coger_llave_sin_llave_en_habitacion(self):
        """coger_llave() no falla si no hay llave."""
        p = self.Personaje()
        p.nombre = "Jugador"
        hab = MagicMock()
        hab.hijos = []
        p.posicion = hab
        try:
            p.coger_llave()
        except Exception as e:
            self.fail(f"coger_llave() lanzo excepcion inesperada: {e}")


# -----------------------------------------------------------------------
# TestEstadoBloqueada
# -----------------------------------------------------------------------

class TestEstadoBloqueada(unittest.TestCase):
    """Tests para el estado Bloqueada (patron State, Media 2)."""

    def setUp(self):
        from EstadoPuerta import Bloqueada, Abierta, Cerrada
        from Llave import Llave
        self.Bloqueada = Bloqueada
        self.Abierta = Abierta
        self.Cerrada = Cerrada
        self.Llave = Llave

    def _make_puerta(self):
        puerta = MagicMock()
        puerta.__str__ = lambda s: "PuertaSalida"
        puerta.lado1 = MagicMock()
        puerta.lado2 = MagicMock()
        return puerta

    def test_bloqueada_es_bloqueada(self):
        estado = self.Bloqueada()
        self.assertTrue(estado.esta_bloqueada())

    def test_bloqueada_no_es_abierta(self):
        estado = self.Bloqueada()
        self.assertFalse(estado.esta_abierta())

    def test_bloqueada_no_es_cerrada(self):
        estado = self.Bloqueada()
        self.assertFalse(estado.esta_cerrada())

    def test_bloqueada_sin_llave_no_pasa(self):
        """Sin llave, el ente no puede pasar."""
        estado = self.Bloqueada()
        puerta = self._make_puerta()
        ente = _Ente()   # inventario vacio
        estado.entrar(ente, puerta)
        puerta.puede_entrar.assert_not_called()

    def test_bloqueada_con_llave_abre_y_pasa(self):
        """Con llave, la puerta se desbloquea y el ente pasa."""
        estado = self.Bloqueada()
        puerta = self._make_puerta()
        ente = _Ente()
        llave = self.Llave()
        llave.recogida = True
        ente.inventario.append(llave)
        estado.entrar(ente, puerta)
        # La puerta debe haber cambiado a Abierta
        self.assertIsInstance(puerta.estado, self.Abierta)

    def test_bloqueada_consume_llave_al_abrir(self):
        """Al abrir la puerta bloqueada, la llave se consume del inventario."""
        estado = self.Bloqueada()
        puerta = self._make_puerta()
        ente = _Ente()
        llave = self.Llave()
        llave.recogida = True
        ente.inventario.append(llave)
        estado.entrar(ente, puerta)
        self.assertEqual(len(ente.inventario), 0)

    def test_desbloquear_cambia_a_abierta(self):
        """desbloquear() transiciona el estado de la puerta a Abierta."""
        estado = self.Bloqueada()
        puerta = self._make_puerta()
        estado.desbloquear(puerta)
        self.assertIsInstance(puerta.estado, self.Abierta)


# -----------------------------------------------------------------------
# TestPuertaSalida
# -----------------------------------------------------------------------

class TestPuertaSalida(unittest.TestCase):
    """Tests para PuertaSalida."""

    def setUp(self):
        from PuertaSalida import PuertaSalida
        from EstadoPuerta import Bloqueada
        self.PuertaSalida = PuertaSalida
        self.Bloqueada = Bloqueada

    def test_puerta_salida_comienza_bloqueada(self):
        p = self.PuertaSalida()
        self.assertIsInstance(p.estado, self.Bloqueada)

    def test_puerta_salida_es_puerta(self):
        p = self.PuertaSalida()
        self.assertTrue(p.es_puerta())

    def test_puerta_salida_es_puerta_salida(self):
        p = self.PuertaSalida()
        self.assertTrue(p.es_puerta_salida())


# -----------------------------------------------------------------------
# TestHabitacionSalida
# -----------------------------------------------------------------------

class TestHabitacionSalida(unittest.TestCase):
    """Tests para HabitacionSalida."""

    def setUp(self):
        from HabitacionSalida import HabitacionSalida
        from Llave import Llave
        self.HabitacionSalida = HabitacionSalida
        self.Llave = Llave

    def test_habitacion_salida_gana_al_entrar(self):
        """Entrar en HabitacionSalida siempre llama a juego.gana_personaje()."""
        hab = self.HabitacionSalida(num=5)
        ente = _Ente()
        hab.entrar(ente)
        ente.juego.gana_personaje.assert_called_once()

    def test_habitacion_salida_gana_sin_llave(self):
        """La llave ya fue consumida por Bloqueada; la victoria es incondicional."""
        hab = self.HabitacionSalida(num=5)
        ente = _Ente()   # inventario vacio
        hab.entrar(ente)
        ente.juego.gana_personaje.assert_called_once()

    def test_habitacion_salida_actualiza_posicion(self):
        hab = self.HabitacionSalida(num=5)
        ente = _Ente()
        hab.entrar(ente)
        self.assertEqual(ente.posicion, hab)

    def test_habitacion_salida_str(self):
        hab = self.HabitacionSalida(num=5)
        self.assertIn("HabitacionSalida", str(hab))


# -----------------------------------------------------------------------
# TestCondicionesFinJuego
# -----------------------------------------------------------------------

class TestCondicionesFinJuego(unittest.TestCase):
    """Tests para las condiciones de fin de juego en Juego."""

    def setUp(self):
        from Juego import Juego
        self.Juego = Juego

    def test_juego_no_terminado_al_inicio(self):
        j = self.Juego()
        self.assertFalse(j.esta_terminado())

    def test_muere_personaje_termina_juego(self):
        j = self.Juego()
        j.person = MagicMock()
        j.person.__str__ = lambda s: "Jugador"
        j.bichos = []
        j.muere_personaje()
        self.assertTrue(j.esta_terminado())

    def test_gana_personaje_termina_juego(self):
        j = self.Juego()
        j.person = MagicMock()
        j.person.__str__ = lambda s: "Jugador"
        j.bichos = []
        j.gana_personaje()
        self.assertTrue(j.esta_terminado())

    def test_muere_personaje_dos_veces_no_falla(self):
        """Llamar dos veces a muere_personaje no causa errores."""
        j = self.Juego()
        j.person = MagicMock()
        j.bichos = []
        j.muere_personaje()
        try:
            j.muere_personaje()
        except Exception as e:
            self.fail(f"Segunda llamada lanzo excepcion: {e}")


# -----------------------------------------------------------------------
# Punto de entrada
# -----------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main(verbosity=2)

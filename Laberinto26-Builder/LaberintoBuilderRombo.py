# LaberintoBuilderRombo: Builder para laberintos con habitaciones rombiformes
from LaberintoBuilder import LaberintoBuilder
from Rombo import Rombo
from Orientaciones import Noreste, Noroeste, Sureste, Suroeste


class LaberintoBuilderRombo(LaberintoBuilder):
    """Builder concreto que construye laberintos con habitaciones rombiformes."""

    def fabricar_noreste(self):  return Noreste()
    def fabricar_noroeste(self): return Noroeste()
    def fabricar_sureste(self):  return Sureste()
    def fabricar_suroeste(self): return Suroeste()

    def fabricar_forma(self):
        forma = Rombo()
        self._asignar_orientaciones(forma)
        return forma

    def _asignar_orientaciones(self, forma):
        """Agrega las 4 orientaciones diagonales a la forma rombiforme."""
        forma.agregar_orientacion(self.fabricar_noreste())
        forma.agregar_orientacion(self.fabricar_noroeste())
        forma.agregar_orientacion(self.fabricar_sureste())
        forma.agregar_orientacion(self.fabricar_suroeste())

    def _map_orientacion(self, nombre: str):
        nombre = str(nombre).capitalize()
        mapping = {
            'Noreste':  self.fabricar_noreste,
            'Noroeste': self.fabricar_noroeste,
            'Sureste':  self.fabricar_sureste,
            'Suroeste': self.fabricar_suroeste,
        }
        if nombre not in mapping:
            raise ValueError(f"Orientacion desconocida: {nombre}")
        return mapping[nombre]()

    def __str__(self):
        return "LaberintoBuilderRombo"

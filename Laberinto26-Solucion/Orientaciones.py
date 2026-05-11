# Implementaciones concretas de Orientacion (Singleton + Bridge)
# Cada clase es un Singleton que sabe como acceder al slot de su direccion en Forma.
from Orientacion import Orientacion


class _SingletonOrientacion(Orientacion):
    """Base comun para todas las orientaciones Singleton."""
    _unica_instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._unica_instancia is None:
            cls._unica_instancia = object.__new__(cls)
        return cls._unica_instancia

    @classmethod
    def default(cls):
        """Devuelve la unica instancia (equivalente al classmethod 'default' de Pharo)."""
        return cls()


# ---------------------------------------------------------------------------
# Orientaciones cardinales (para Cuadrado: norte/sur/este/oeste)
# ---------------------------------------------------------------------------

class Norte(_SingletonOrientacion):
    """Orientacion Norte: accede al slot 'norte' de Cuadrado."""

    def obtener_elemento(self, forma):
        return forma.norte

    def poner_elemento(self, em, forma):
        forma.norte = em

    def caminar(self, bicho):
        em = bicho.posicion.forma.norte
        em.entrar(bicho)

    def aceptar(self, visitor, forma):
        if forma.norte:
            forma.norte.aceptar(visitor)

    def recorrer(self, bloque, forma):
        if forma.norte:
            forma.norte.recorrer(bloque)

    def __str__(self):  return "Norte"
    def __repr__(self): return "Norte"


class Sur(_SingletonOrientacion):
    """Orientacion Sur: accede al slot 'sur' de Cuadrado."""

    def obtener_elemento(self, forma):
        return forma.sur

    def poner_elemento(self, em, forma):
        forma.sur = em

    def caminar(self, bicho):
        em = bicho.posicion.forma.sur
        em.entrar(bicho)

    def aceptar(self, visitor, forma):
        if forma.sur:
            forma.sur.aceptar(visitor)

    def recorrer(self, bloque, forma):
        if forma.sur:
            forma.sur.recorrer(bloque)

    def __str__(self):  return "Sur"
    def __repr__(self): return "Sur"


class Este(_SingletonOrientacion):
    """Orientacion Este: accede al slot 'este' de Cuadrado."""

    def obtener_elemento(self, forma):
        return forma.este

    def poner_elemento(self, em, forma):
        forma.este = em

    def caminar(self, bicho):
        em = bicho.posicion.forma.este
        em.entrar(bicho)

    def aceptar(self, visitor, forma):
        if forma.este:
            forma.este.aceptar(visitor)

    def recorrer(self, bloque, forma):
        if forma.este:
            forma.este.recorrer(bloque)

    def __str__(self):  return "Este"
    def __repr__(self): return "Este"


class Oeste(_SingletonOrientacion):
    """Orientacion Oeste: accede al slot 'oeste' de Cuadrado."""

    def obtener_elemento(self, forma):
        return forma.oeste

    def poner_elemento(self, em, forma):
        forma.oeste = em

    def caminar(self, bicho):
        em = bicho.posicion.forma.oeste
        em.entrar(bicho)

    def aceptar(self, visitor, forma):
        if forma.oeste:
            forma.oeste.aceptar(visitor)

    def recorrer(self, bloque, forma):
        if forma.oeste:
            forma.oeste.recorrer(bloque)

    def __str__(self):  return "Oeste"
    def __repr__(self): return "Oeste"


# ---------------------------------------------------------------------------
# Orientaciones diagonales (para Rombo: ne/no/se/so)
# ---------------------------------------------------------------------------

class Noreste(_SingletonOrientacion):
    """Orientacion Noreste: accede al slot 'ne' de Rombo."""

    def obtener_elemento(self, forma):
        return forma.ne

    def poner_elemento(self, em, forma):
        forma.ne = em

    def caminar(self, bicho):
        em = bicho.posicion.forma.ne
        em.entrar(bicho)

    def aceptar(self, visitor, forma):
        if forma.ne:
            forma.ne.aceptar(visitor)

    def recorrer(self, bloque, forma):
        if forma.ne:
            forma.ne.recorrer(bloque)

    def __str__(self):  return "Noreste"
    def __repr__(self): return "Noreste"


class Noroeste(_SingletonOrientacion):
    """Orientacion Noroeste: accede al slot 'no' de Rombo."""

    def obtener_elemento(self, forma):
        return forma.no

    def poner_elemento(self, em, forma):
        forma.no = em

    def caminar(self, bicho):
        em = bicho.posicion.forma.no
        em.entrar(bicho)

    def aceptar(self, visitor, forma):
        if forma.no:
            forma.no.aceptar(visitor)

    def recorrer(self, bloque, forma):
        if forma.no:
            forma.no.recorrer(bloque)

    def __str__(self):  return "Noroeste"
    def __repr__(self): return "Noroeste"


class Sureste(_SingletonOrientacion):
    """Orientacion Sureste: accede al slot 'se' de Rombo."""

    def obtener_elemento(self, forma):
        return forma.se

    def poner_elemento(self, em, forma):
        forma.se = em

    def caminar(self, bicho):
        em = bicho.posicion.forma.se
        em.entrar(bicho)

    def aceptar(self, visitor, forma):
        if forma.se:
            forma.se.aceptar(visitor)

    def recorrer(self, bloque, forma):
        if forma.se:
            forma.se.recorrer(bloque)

    def __str__(self):  return "Sureste"
    def __repr__(self): return "Sureste"


class Suroeste(_SingletonOrientacion):
    """Orientacion Suroeste: accede al slot 'so' de Rombo."""

    def obtener_elemento(self, forma):
        return forma.so

    def poner_elemento(self, em, forma):
        forma.so = em

    def caminar(self, bicho):
        em = bicho.posicion.forma.so
        em.entrar(bicho)

    def aceptar(self, visitor, forma):
        if forma.so:
            forma.so.aceptar(visitor)

    def recorrer(self, bloque, forma):
        if forma.so:
            forma.so.recorrer(bloque)

    def __str__(self):  return "Suroeste"
    def __repr__(self): return "Suroeste"

# Contenedor es un ElementoMapa que tiene hijos (Composite).
# Implementa el puente Bridge delegando en su Forma.
from ElementoMapa import ElementoMapa


class Contenedor(ElementoMapa):
    """Es-un ElementoMapa que tiene-una Forma (Bridge) y una lista de hijos (Composite)."""

    def __init__(self):
        super().__init__()
        self.hijos = []     # bombas, tuneles, armarios hijos
        self.forma = None   # Cuadrado o Rombo (Bridge)
        self.num = 0

    # --- Visitor ---
    def aceptar(self, visitor):
        """Acepta visitante: se visita a si mismo, luego hijos y luego elementos de orientacion."""
        self.aceptar_contenedor(visitor)
        for hijo in self.hijos:
            hijo.aceptar(visitor)
        for or_ in self.forma.orientaciones:
            or_.aceptar(visitor, self.forma)

    def aceptar_contenedor(self, visitor):
        """Metodo abstracto que las subclases concretas deben implementar."""
        raise NotImplementedError(
            f"{self.__class__.__name__} debe implementar aceptar_contenedor")

    # --- Gestion de hijos ---
    def agregar_hijo(self, em):
        """Anade un hijo (bomba, tunel, armario) a este contenedor."""
        self.hijos.append(em)

    def eliminar_hijo(self, em):
        """Elimina un hijo; devuelve None si no existe (como ifAbsent en Pharo)."""
        if em in self.hijos:
            self.hijos.remove(em)

    # --- Gestion de orientaciones (delegadas a Forma) ---
    def agregar_orientacion(self, or_):
        self.forma.agregar_orientacion(or_)

    def eliminar_orientacion(self, or_):
        self.forma.eliminar_orientacion(or_)

    @property
    def orientaciones(self):
        """Orientaciones del contenedor (delegadas a la Forma)."""
        return self.forma.orientaciones if self.forma else []

    # --- Acceso Bridge ---
    def obtener_elemento(self, una_or):
        """Obtiene el ElementoMapa en la direccion indicada (Bridge)."""
        return self.forma.obtener_elemento(una_or)

    def poner_en(self, una_or, em):
        """Coloca un ElementoMapa en la direccion indicada (Bridge)."""
        self.forma.poner_en(una_or, em)

    def obtener_orientacion_aleatoria(self):
        """Devuelve una orientacion aleatoria de la Forma."""
        return self.forma.obtener_orientacion_aleatoria()

    # --- Busqueda ---
    def buscar_tunel(self):
        """Devuelve el tunel hijo si existe."""
        for hijo in self.hijos:
            if hijo.es_tunel():
                return hijo
        return None

    # --- Comportamiento ---
    def entrar(self, alguien):
        """Cuando alguien entra en el contenedor: imprime y actualiza posicion."""
        print(f"{alguien} esta en {self}")
        alguien.posicion = self

    def recorrer(self, bloque):
        """Recorre este contenedor, sus hijos y los elementos de sus orientaciones."""
        print(str(self))
        bloque(self)
        for hijo in self.hijos:
            hijo.recorrer(bloque)
        for or_ in self.forma.orientaciones:
            or_.recorrer(bloque, self.forma)

    def __str__(self):
        return f"{self.__class__.__name__}-{self.num}"


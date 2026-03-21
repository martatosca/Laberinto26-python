from Varita import Varita

class BichoAdapter(Varita):
    """
    ADAPTER del patrón Adapter.
    
    Adapta la interfaz del Bicho (Adaptee) a la interfaz de Varita (Target).
    Permite que el Personaje use una Varita para cambiar el modo de un Bicho.
    
    - Target: Varita (interfaz esperada por el Client)
    - Adaptee: Bicho (interfaz existente que necesita ser adaptada)
    - Adapter: BichoAdapter (adapta Bicho a Varita)
    - Client: Personaje (usa la Varita)
    """
    
    def __init__(self, bicho):
        """
        El Adapter mantiene una referencia al Adaptee (composición).
        """
        self._bicho = bicho
    
    @property
    def bicho(self):
        return self._bicho
    
    @bicho.setter
    def bicho(self, value):
        self._bicho = value
    
    def cambiar_modo(self):
        """
        Implementa la interfaz Target (Varita).
        Delega al Adaptee (Bicho) llamando a su modo.cambiar_modo().
        """
        if self._bicho and self._bicho.modo:
            # Delega al modo del bicho para que cambie
            nuevo_modo = self._bicho.modo.cambiar_modo(self._bicho)
            return nuevo_modo
        return None
    
    def __str__(self):
        return f"BichoAdapter({self._bicho})"

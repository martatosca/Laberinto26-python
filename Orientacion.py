from abc import ABC, abstractmethod

class Orientacion(ABC):
    """
    Strategy abstracto para las orientaciones de una habitación.
    Define la interfaz común para todas las orientaciones.
    """
    
    @abstractmethod
    def obtener_nombre(self) -> str:
        """Devuelve el nombre de la orientación"""
        pass
    
    @abstractmethod
    def obtener_opuesta(self) -> "Orientacion":
        """Devuelve la orientación opuesta"""
        pass
    
    def caminar(self, bicho):
        """
        Hace que el bicho camine en esta orientación.
        Obtiene el elemento en esta orientación y hace que el bicho entre.
        Según código del profesor: or caminar:unBicho
        """
        if bicho.posicion is None:
            print(f"{bicho.nombre} no tiene posición")
            return
        
        # Obtener el elemento en esta orientación de la habitación actual
        elemento = bicho.posicion.obtener_en(self)
        if elemento:
            print(f"{bicho.nombre} camina hacia el {self.obtener_nombre()}")
            elemento.entrar(bicho)
        else:
            print(f"No hay salida hacia el {self.obtener_nombre()}")
    
    def __str__(self):
        return self.obtener_nombre()

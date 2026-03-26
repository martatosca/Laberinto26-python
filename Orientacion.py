from abc import ABC, abstractmethod

class Orientacion(ABC):
    
    
    @abstractmethod
    def obtener_nombre(self) -> str:
        
        pass
    
    @abstractmethod
    def obtener_opuesta(self) -> "Orientacion":
        
        pass
    
    def caminar(self, bicho):
        
        if bicho.posicion is None:
            print(f"{bicho.nombre} no tiene posición")
            return
        
        elemento = bicho.posicion.obtener_en(self)
        if elemento:
            print(f"{bicho.nombre} camina hacia el {self.obtener_nombre()}")
            elemento.entrar(bicho)
        else:
            print(f"No hay salida hacia el {self.obtener_nombre()}")
    
    def __str__(self):
        return self.obtener_nombre()

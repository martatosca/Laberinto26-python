from abc import ABC, abstractmethod

class Modo(ABC):
    
    
    def actua(self, bicho) -> str:
        
        print(f"\n[{bicho.nombre}] ejecutando secuencia de acciones ({self.obtener_nombre()})...")
        resultados = []
        resultados.append(self.atacar(bicho))
        resultados.append(self.duerme(bicho))
        print(f"[{bicho.nombre}] secuencia completada.")
        return "\n".join(resultados)
    
    @abstractmethod
    def atacar(self, bicho) -> str:
        
        pass
    
    @abstractmethod
    def duerme(self, bicho) -> str:
        
        pass
    
    @abstractmethod
    def caminar(self, bicho) -> str:
        
        pass
    
    def camina(self, bicho):
        
        if bicho.posicion is None:
            print(f"{bicho.nombre} no tiene posición")
            return
        
        orientacion = bicho.posicion.obtener_orientacion_aleatoria()
        if orientacion:
            self.caminar(bicho)
            orientacion.caminar(bicho)
        else:
            print(f"{bicho.nombre} no puede moverse (sin orientaciones)")
    
    @abstractmethod
    def obtener_nombre(self) -> str:
        
        pass
    
    @abstractmethod
    def cambiar_modo(self, bicho):
        
        pass
    
    def __str__(self):
        return self.obtener_nombre()

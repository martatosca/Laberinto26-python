from abc import ABC, abstractmethod

class Modo(ABC):
    """
    AbstractClass del patrón Template Method + Strategy.
    Define el esqueleto del algoritmo en actua() y delega pasos a las subclases.
    """
    
    # ==================== TEMPLATE METHOD ====================
    def actua(self, bicho) -> str:
        """
        TEMPLATE METHOD: Define el esqueleto del algoritmo.
        Llama a las operaciones primitivas en orden definido.
        Las subclases NO deben sobrescribir este método.
        """
        print(f"\n[{bicho.nombre}] ejecutando secuencia de acciones ({self.obtener_nombre()})...")
        resultados = []
        resultados.append(self.atacar(bicho))   # Paso 1: Atacar
        resultados.append(self.duerme(bicho))   # Paso 2: Dormir
        print(f"[{bicho.nombre}] secuencia completada.")
        return "\n".join(resultados)
    
    # ==================== OPERACIONES PRIMITIVAS ====================
    @abstractmethod
    def atacar(self, bicho) -> str:
        """Operación primitiva: Define cómo ataca el bicho según este modo"""
        pass
    
    @abstractmethod
    def duerme(self, bicho) -> str:
        """Operación primitiva: Define cómo duerme el bicho según este modo"""
        pass
    
    # ==================== OTROS MÉTODOS ====================
    @abstractmethod
    def caminar(self, bicho) -> str:
        """Define cómo camina el bicho según este modo (estilo)"""
        pass
    
    def camina(self, bicho):
        """
        Según código del profesor:
        Modo>>camina:unBicho
            | or |
            or:=unBicho posicion obtenerOrientacionAleatoria.
            or caminar:unBicho.
        
        Obtiene orientación aleatoria de la habitación y hace que el bicho camine.
        """
        if bicho.posicion is None:
            print(f"{bicho.nombre} no tiene posición")
            return
        
        # Obtener orientación aleatoria de la posición actual
        orientacion = bicho.posicion.obtener_orientacion_aleatoria()
        if orientacion:
            self.caminar(bicho)  # Primero muestra el estilo de caminar
            orientacion.caminar(bicho)  # Luego mueve al bicho
        else:
            print(f"{bicho.nombre} no puede moverse (sin orientaciones)")
    
    @abstractmethod
    def obtener_nombre(self) -> str:
        """Devuelve el nombre del modo"""
        pass
    
    @abstractmethod
    def cambiar_modo(self, bicho):
        """
        Adapter: Cambia el modo del bicho al modo opuesto.
        Agresivo -> Perezoso, Perezoso -> Agresivo
        """
        pass
    
    def __str__(self):
        return self.obtener_nombre()

from Pared import Pared

class ParedFuego(Pared):
    
    
    def __init__(self, intensidad: int = 5):
        super().__init__()
        self.intensidad = intensidad
        self.encendida = True
    
    def entrar(self):
        if self.encendida:
            print(f"🔥 ¡La pared está en llamas! Te quemas. Daño: {self.intensidad}")
        else:
            print("La pared de fuego está apagada.")
    
    def apagar(self):
        
        self.encendida = False
        print("El fuego se ha apagado.")
    
    def encender(self):
        
        self.encendida = True
        print("El fuego se ha encendido.")
    
    def __str__(self):
        estado = "encendida" if self.encendida else "apagada"
        return f"ParedFuego ({estado}, intensidad={self.intensidad})"

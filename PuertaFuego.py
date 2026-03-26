from Puerta import Puerta

class PuertaFuego(Puerta):
    
    
    def __init__(self, lado1=None, lado2=None, abierta=False, intensidad: int = 3):
        super().__init__(lado1, lado2, abierta)
        self.intensidad = intensidad
        self.encendida = True
    
    def entrar(self):
        if self.encendida:
            if self.abierta:
                print(f"🔥 Has pasado por la puerta en llamas. ¡Te quemas! Daño: {self.intensidad}")
            else:
                print(f"🔥 La puerta está cerrada y en llamas. ¡Te quemas al tocarla! Daño: {self.intensidad}")
        else:
            if self.abierta:
                print("Has pasado por la puerta (el fuego está apagado).")
            else:
                print("La puerta está cerrada, no puedes pasar.")
    
    def apagar(self):
        
        self.encendida = False
        print("El fuego de la puerta se ha apagado.")
    
    def encender(self):
        
        self.encendida = True
        print("El fuego de la puerta se ha encendido.")
    
    def __str__(self):
        estado_fuego = "🔥" if self.encendida else "apagada"
        estado_puerta = "abierta" if self.abierta else "cerrada"
        return f"PuertaFuego ({estado_puerta}, {estado_fuego})"

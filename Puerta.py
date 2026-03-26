from Hoja import Hoja
class Puerta(Hoja):
    def __init__(self, lado1, lado2, abierta=False):
        super().__init__()
        self.abierta=abierta
        self.lado1=lado1
        self.lado2=lado2
    
  
    def setAbierta(self, abierta):
        self.abierta=abierta
    
    def setLado1(self, lado1):
        self.lado1 = lado1
    
    def setLado2(self, lado2):
        self.lado2 = lado2
    
    def entrar(self, alguien=None):
        
        if alguien:
            if self.abierta:
                if alguien.posicion == self.lado1:
                    self.lado2.entrar(alguien)
                else:
                    self.lado1.entrar(alguien)
            else:
                print("La puerta está cerrada")
        else:
            if self.abierta:
                print("Has pasado por la puerta")
            else:
                print("La puerta está cerrada, no puedes pasar")
    
    def es_puerta(self):
        
        return True
    
    def abrir(self):
        self.abierta=True
        
    def cerrar(self):
        self.abierta=False
        
    def __str__(self):
        return "Puerta abierta" if self.abierta else "Puerta cerrada"

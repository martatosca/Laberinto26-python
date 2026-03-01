from Hoja import Hoja
#Representa una puerta, es un elemento del mapa que puede estar abierta o cerrada
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
    
    def entrar(self):
        if self.abierta:
            print("Has pasado por la puerta")
        else:
            print("La puerta está cerrada, no puedes pasar")
    def abrir(self):
        self.abierta=True
        
    def cerrar(self):
        self.abierta=False
        
    def __str__(self):
        return "Puerta abierta" if self.abierta else "Puerta cerrada"
    
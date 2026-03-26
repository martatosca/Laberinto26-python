from Puerta import Puerta

class PuertaBomba(Puerta):
    
    
    def __init__(self, lado1=None, lado2=None, abierta=False, activa=True):
        super().__init__(lado1, lado2, abierta)
        self.activa = activa
    
    def entrar(self):
        if self.activa:
            print("💥 ¡BOOM! La puerta bomba ha explotado al intentar pasar.")
            self.activa = False
            self.abierta = True
        elif self.abierta:
            print("Has pasado por la puerta (la bomba ya explotó).")
        else:
            print("La puerta bomba está cerrada, no puedes pasar.")
    
    def abrir(self):
        if self.activa:
            print("💥 ¡BOOM! La puerta bomba ha explotado al intentar abrirla.")
            self.activa = False
            self.abierta = True
        else:
            self.abierta = True
    
    def __str__(self):
        if self.activa:
            return "PuertaBomba (activa)"
        elif self.abierta:
            return "PuertaBomba (explotada, abierta)"
        else:
            return "PuertaBomba (desactivada, cerrada)"

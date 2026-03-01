from Hoja import Hoja
#Esta clase representa una pared de un labetinto, es una hoja porque no tiene hijos
class Pared(Hoja):
    def __init__(self):
        super().__init__()
        
    def entrar(self):
        print("Has chocado contra una pared")
        
    def __str__(self):
        return "Pared"
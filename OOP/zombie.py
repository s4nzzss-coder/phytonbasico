from Enemigo import *

class zombie(Enemigo):
    def __init__(self, tipo_enemigo, puntos_energia=10, ataque=1):
        super().__init__(tipo_enemigo, 'zombie', puntos_energia, ataque)

    def habla(self):
        print("Hummm....*")

    def propagar_enfermedad(self):
        print("El zombie está tratando de propagar la enfermedad!!")
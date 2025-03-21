class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

class Volador:
    def volar(self):
        print(f"{self.nombre} está volando.")

class Murcielago(Animal, Volador):
    def __init__(self, nombre):
        
        Animal.__init__(self, nombre)

murcielago = Murcielago("Bruce")

murcielago.comer()
murcielago.volar()
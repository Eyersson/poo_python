# Composición

"""Una coordenada en dos dimensiones está compuesta por dos valores, el valor en el eje x y el valor en el eje de las y, ésto podría ser una clase. Un cuadrado está compuesto por cuatro coordenadas que son los cuatro vértices, esto podría ser una clase que está compuesta por cuatro clases del objeto coordenada."""

# Clase Coordenada

class coordenada:

    def __init__(self, x , y):
        self, x = x
        self, y = y

def mostrarcoordenada(self):
      def mostrarcoordenada(self):
        print("(", self.X, ",", self.Y, ")")

# clase cuadrado

class Cuadrado:
    # método constructor

    def __init__(self, v1, v2, v3, v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

    # metodo para mostrar los vertices

    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.v1.mostrarcoordenada()
        self.v2.mostrarcoordenada()
        self.v3.mostrarcoordenada()
        self.v4.mostrarcoordenada()

# metodo principal

def main ():
    # input
    x1 = int(input("Digite el valor de x: "))
    x2 = int(input("Digite el valor de y: "))

    c1 = coordenada(x1,x2)
    c1.mostrarcoordenada()

    v1 = coordenada(7,8)
    v2 = coordenada(10,8)
    v3 = coordenada(7,5)
    v4 = coordenada(10,5)

    cuadrado1 = Cuadrado(v1, v2, v3, v4)
    cuadrado1.mostrarVertices()



if __name__ == "__main__":
    main()
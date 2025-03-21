# composicion

"""una coordenada en dos dimenciones esta compuesta por dos valores, el valor en el eje de las x y el valor en el eje de las y, esta podria ser una clase.un cuadrado esta compuesto por cuatro coordenadas que son los cuatros vertises, esto podria ser una clase que esta compuesta por cuatro clases del objeto coordenada"""

# clase coordenada

class Coordenada:

    # metodo constructor
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y

    def getX(self):
        return self.__X
    
    def getY(self):
        return self.__Y

    def setX(self, x):
        self.__X = x

    def setY(self, y):
        self.__Y = y

    def mostrarCoordenada(self):
        print("(", self.__X, ",", self.__Y, ")")

# clase cuadrado

class Cuadrado:

    def __init__(self,v1, v2, v3, v4):
        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4
        
    def __mostrarCoodenadaV1(self):
        print("(", self.__V1.getX(), ",", self.__V1.getY(),")")

    def __mostrarCoodenadaV2(self):
        print("(", self.__V2.getX(), ",", self.__V2.getY(),")")

    def __mostrarCoodenadaV3(self):
        print("(", self.__V3.getX(), ",", self.__V3.getY(),")")

    def __mostrarCoodenadaV4(self):
        print("(", self.__V4.getX(), ",", self.__V4.getY(),")")

    def mostrarVertices(self):
        print("el cuadrado esta compuesto por los siguientes vertice: ")
        self.__mostrarCoordenadaV1()
        self.__mostrarCoordenadaV2()
        self.__mostrarCoordenadaV3()
        self.__mostrarCoordenadaV4()

# metodo principal
def main():
    # input
    x1 = int(input("digite el valor de x: "))
    x2 = int(input("digite el valor de y: "))

    # prosessing
    c1 = Coordenada(x1, x2)
    c1.mostrarCoordenada()

    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)    
    v4 = Coordenada(10,5)

    cuadrado1 = Cuadrado(v1, v2, v3 ,v4)
    cuadrado1.mostrarVertices()
    

if __name__ == "__main__":
    main()


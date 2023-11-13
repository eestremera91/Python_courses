from os import system

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.altura*self.base

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)




def run():
    rectangulo = Rectangulo(3,4)
    print(rectangulo.area())

    cuadrado = Cuadrado(5)
    print(cuadrado.area())


if  __name__  ==  '__main__' :
    system('cls')
    run()
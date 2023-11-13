from os import system

class persona:
    def __init__(self, nombre):
        self.nombre= nombre

    def avanza(self):
        print('Ando caminando')

class ciclista(persona):
    def __init__ (self,nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Me muevo en bicicleta')


def run():
    persona1 = persona('David')
    persona1.avanza()

    ciclista1 = ciclista('Daniel')
    ciclista1.avanza()


if  __name__  ==  '__main__' :
    system('cls')
    run()
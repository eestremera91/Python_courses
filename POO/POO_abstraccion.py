from os import system

class lavadora:
    def __init__(self):
        pass

    def lavar(self,temperatura='caliente'):
        self._llenar_tanque_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_agua(self, temperatura):
        print('Llenando el tanque con agua '+ temperatura)

    def _anadir_jabon(self):
        print('Anadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')



def run():
    lavadora1 = lavadora()
    lavadora1.lavar()


if  __name__  ==  '__main__' :
    system('cls')
    run()